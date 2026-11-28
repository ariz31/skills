#!/usr/bin/env python3
"""Build deterministic standalone skill directories or ZIP archives."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from validate_registry import ID, frontmatter, resolve_path, validate


def source_revision(root):
    try:
        revision = subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True,stderr=subprocess.DEVNULL).strip()
        if subprocess.check_output(["git","status","--porcelain","--untracked-files=no"],cwd=root,text=True).strip():
            return revision + "-dirty"
        return revision
    except (OSError,subprocess.CalledProcessError):
        return None


def package_files(root, s, target, platform, bundle, include_evals):
    directory=resolve_path(root,s["path"]).parent
    files={}
    def add(path, dest=None):
        src=resolve_path(root,path)
        if not src.is_relative_to(directory) and path!="docs/INVARIANTS.md":
            raise ValueError("file escapes skill package: "+path)
        dest=dest or src.relative_to(directory).as_posix()
        if dest in files: raise ValueError("duplicate destination "+dest)
        files[dest]=src.read_bytes()
    add(s["path"])
    if target!=s["id"]:
        body=files["SKILL.md"].decode("utf-8")
        body,n=re.subn(r"(?m)^name:\s*[^\n]+$", "name: "+target, body,count=1)
        if n!=1 or frontmatter(body).get("name")!=target:
            raise ValueError("cannot rename frontmatter")
        files["SKILL.md"]=body.encode()
    for path in s["references"]: add(path)
    for key,path in sorted(s["adapters"].items()):
        if platform=="portable" or platform==key: add(path)
    if bundle:
        add("docs/INVARIANTS.md","references/invariants.md")
        # Link the offline copy from the installed skill without changing canonical content.
        body=files["SKILL.md"].decode("utf-8")
        end=body.index("\n---",3)+4
        body=body[:end]+"\n\nApply the bundled [library invariants](references/invariants.md)."+body[end:]
        files["SKILL.md"]=body.encode("utf-8")
    if include_evals:
        add(str((directory/"evaluations/SCENARIOS.md").relative_to(root)))
    # Remove package-local links to intentionally omitted optional adapters/evaluations,
    # retaining their visible label and indicating that the resource was not bundled.
    for dest,raw in list(files.items()):
        if not dest.endswith(".md"): continue
        body=raw.decode("utf-8")
        def rewrite(match):
            label, link=match.groups()
            bare=link.split("#",1)[0]
            if not bare or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",bare): return match.group(0)
            path=(Path(dest).parent/ bare).as_posix()
            if path not in files and (path.startswith("adapters/") or path.startswith("evaluations/") or path=="references/invariants.md"):
                return label+" (not bundled; see canonical repository)"
            if dest=="references/invariants.md" and bare=="INSTALLATION.md":
                return label+" (see canonical repository)"
            return match.group(0)
        files[dest]=re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",rewrite,body).encode("utf-8")
    return files


def main():
    p=argparse.ArgumentParser(description=__doc__)
    group=p.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill",action="append")
    group.add_argument("--all",action="store_true")
    p.add_argument("--registry",type=Path,default=Path("registry.json"))
    p.add_argument("--output-dir",type=Path,default=Path("/tmp/ariz31_staged"))
    p.add_argument("--format",choices=("dir","zip"),default="dir")
    p.add_argument("--platform",choices=("gemini-task","chatgpt-work","portable"),default="portable")
    p.add_argument("--rename")
    p.add_argument("--bundle-invariants",action=argparse.BooleanOptionalAction,default=None)
    p.add_argument("--include-evals",action="store_true")
    p.add_argument("--allow-draft",action="store_true")
    p.add_argument("--dry-run",action="store_true")
    a=p.parse_args()
    if a.rename and (a.all or len(a.skill)!=1 or not ID.fullmatch(a.rename)):
        p.error("--rename requires a single --skill and lowercase kebab-case name")
    registry_path=a.registry.resolve()
    root=registry_path.parent
    try:
        registry=json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError,ValueError) as exc:
        print(str(exc),file=sys.stderr); return 2
    checked=validate(root,registry)
    if checked["errors"]:
        print(json.dumps(checked,indent=2),file=sys.stderr); return 1
    skills={s["id"]:s for s in registry["skills"]}
    aliases={}
    for k,s in skills.items():
        for token in [k]+s["triggers"]:
            token=token.lower().lstrip("@/")
            if ID.fullmatch(token):
                aliases.setdefault(token,set()).add(k)
    try:
        targets=[]
        if a.all: targets=[k for k,s in skills.items() if s["status"]=="active"]
        else:
            for token in a.skill:
                normalized=token.lower().lstrip("@/")
                options={normalized} if normalized in skills else aliases.get(normalized,set())
                if len(options)!=1: raise ValueError("unknown or ambiguous skill: "+token)
                k=next(iter(options))
                if k not in targets: targets.append(k)
        for k in targets:
            if skills[k]["status"]!="active" and not (a.allow_draft and skills[k]["status"]=="draft"):
                raise ValueError("non-active skill: "+k)
        out=a.output_dir.resolve()
        bundle=a.bundle_invariants if a.bundle_invariants is not None else a.platform=="gemini-task"
        revision=source_revision(root)
        summary=[]
        for k in targets:
            s=skills[k]; target=a.rename or k
            if a.rename and target!=k and target in skills:
                raise ValueError("rename collides with canonical skill: "+target)
            stage=out/target
            archive=out/f"{target}-v{s['version']}.zip"
            # Never overwrite source paths or an ancestor of the repository.
            for dest in (stage,archive):
                if dest.resolve().is_relative_to(root/"skills") or root.is_relative_to(dest.resolve()) or dest.resolve() in {root/"docs",root/"scripts",root/"platforms",root/".github",root/"evaluations"}:
                    raise ValueError("unsafe output path: "+str(dest))
                if dest.is_symlink(): raise ValueError("refuse symlink output: "+str(dest))
            files=package_files(root,s,target,a.platform,bundle,a.include_evals)
            manifest={"schema_version":1,"id":target,"name":s["name"],"version":s["version"],
                      "platform":a.platform,"source_repo":registry["library"],"source_commit":revision,
                      "required_dependencies":s["required_dependencies"],"optional_dependencies":s["optional_dependencies"],
                      "files":{name:"sha256:"+hashlib.sha256(raw).hexdigest() for name,raw in sorted(files.items())}}
            if target!=k: manifest["source_id"]=k
            files["PACKAGE_MANIFEST.json"]=(json.dumps(manifest,indent=2,sort_keys=True)+"\n").encode()
            dest=archive if a.format=="zip" else stage
            if not a.dry_run:
                out.mkdir(parents=True,exist_ok=True)
                with tempfile.TemporaryDirectory(prefix=".skill-stage-",dir=out) as tmp:
                    temp=Path(tmp)
                    if a.format=="zip":
                        candidate=temp/archive.name
                        with zipfile.ZipFile(candidate,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
                            for name,raw in sorted(files.items()):
                                info=zipfile.ZipInfo(target+"/"+name,date_time=(1980,1,1,0,0,0))
                                info.compress_type=zipfile.ZIP_DEFLATED
                                info.external_attr=0o100644<<16
                                z.writestr(info,raw,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
                        candidate.replace(archive)
                    else:
                        candidate=temp/target; candidate.mkdir()
                        for name,raw in sorted(files.items()):
                            f=candidate/name; f.parent.mkdir(parents=True,exist_ok=True); f.write_bytes(raw)
                        if stage.exists():
                            if not stage.is_dir() or not (stage/"PACKAGE_MANIFEST.json").is_file():
                                raise ValueError("refusing to replace non-package directory: "+str(stage))
                            shutil.rmtree(stage)
                        candidate.replace(stage)
            summary.append({"id":target,"version":s["version"],"path":str(dest),"required_dependencies":s["required_dependencies"],"files":sorted(files)})
        print(json.dumps({"dry_run":a.dry_run,"packages":summary},indent=2))
        return 0
    except ValueError as exc:
        print(str(exc),file=sys.stderr); return 1
    except OSError as exc:
        print(str(exc),file=sys.stderr); return 2


if __name__=="__main__":
    sys.exit(main())
