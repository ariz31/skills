#!/usr/bin/env python3
"""Validate portable skill registry, package paths, and deterministic routing."""
import argparse
import json
from pathlib import Path
import re
import sys

ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
FIELDS = set("id name version status category subcategory path description triggers tags outputs required_dependencies optional_dependencies capabilities platforms references adapters".split())
CATEGORIES = set("explicit_command alias semantic_positive composition conditional_dependency negative_non_trigger install_protocol read_only_guard".split())
MODES = set("execute clarify_first install sync update ordinary_assistance".split())


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening YAML fence")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing YAML fence") from exc
    result = {}
    i = 1
    while i < end:
        line = lines[i]
        i += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z][\w-]*):\s*(.*)", line)
        if not match:
            raise ValueError("unsupported frontmatter line: " + line)
        key, value = match.groups()
        if key in result:
            raise ValueError("duplicate frontmatter key: " + key)
        if value in (">", ">-", ">+", "|", "|-", "|+"):
            parts = []
            while i < end and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                parts.append(lines[i].strip())
                i += 1
            value = ("\n" if value.startswith("|") else " ").join(parts).strip()
        elif value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                raise ValueError("invalid quoted frontmatter") from exc
        elif value.startswith("'"):
            if not value.endswith("'"):
                raise ValueError("invalid quoted frontmatter")
            value = value[1:-1].replace("''", "'")
        if not isinstance(value, str):
            raise ValueError("frontmatter values must be strings")
        result[key] = value
    return result


def string_list(value):
    return isinstance(value, list) and all(isinstance(x, str) and x for x in value)


def resolve_path(root, value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("invalid repository-relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe repository-relative path: " + value)
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root) or not resolved.is_file():
        raise ValueError("missing or escaped file: " + value)
    return resolved


def dependency_order(skills, targets, optional=False):
    order, visiting, done = [], [], set()
    def visit(key):
        if key in visiting:
            raise ValueError("cycle: " + " -> ".join(visiting[visiting.index(key):] + [key]))
        if key in done:
            return
        if key not in skills:
            raise ValueError("unknown dependency: " + key)
        visiting.append(key)
        s = skills[key]
        edges = s.get("required_dependencies", [])
        if optional:
            edges = edges + s.get("optional_dependencies", [])
        for dep in edges:
            visit(dep)
        visiting.pop()
        done.add(key)
        order.append(key)
    for key in targets:
        visit(key)
    return order


def alias_map(skills):
    aliases = {}
    for key, s in skills.items():
        if s["status"] != "active":
            continue
        for token in [key] + s["triggers"]:
            normalized = token.lower().lstrip("@/")
            if ID.fullmatch(normalized):
                if normalized in aliases and aliases[normalized] != key:
                    raise ValueError("ambiguous alias: " + normalized)
                aliases[normalized] = key
    return aliases


def deterministic_route(prompt, skills):
    aliases = alias_map(skills)
    command = re.match(r"^\s*(install|sync|update)\s+ariz31/skills(?:\s+(.*))?\s*$", prompt, re.I)
    if command:
        mode, tail = command.group(1).lower(), command.group(2)
        if tail:
            targets = [aliases[x.lower().lstrip("@/")] for x in re.split(r"[\s,]+", tail.strip()) if x]
        elif mode == "install":
            targets = [k for k,s in skills.items() if s["status"] == "active"]
        else:
            # Sync/update without IDs require a runtime inventory, not a guessed selection.
            targets = []
        return mode, dependency_order(skills, targets)
    explicit = []
    commands = {t.lower(): k for k,s in skills.items() if s["status"] == "active"
                for t in s["triggers"] if t.startswith(("@", "/"))}
    for token in re.findall(r"(?<![\w@/])[@/][a-z0-9]+(?:-[a-z0-9]+)*(?![\w-])", prompt.lower()):
        if token in commands and commands[token] not in explicit:
            explicit.append(commands[token])
    return ("clarify_first" if "ask" in explicit else "execute"), dependency_order(skills, explicit)


def validate(root, registry, maximum=800, warning=750, trigger_file=None):
    errors, warnings, counts = [], [], {}
    skills = {}
    def issue(rule, message, skill=None, path=None, warn=False):
        item = {"rule": rule, "message": message}
        if skill is not None: item["skill_id"] = skill
        if path is not None: item["path"] = str(path)
        (warnings if warn else errors).append(item)
    def check_path(rule, value, skill=None):
        try:
            return resolve_path(root, value)
        except (ValueError, OSError) as exc:
            issue(rule, str(exc), skill, value)
            return None
    if not isinstance(registry, dict):
        issue("V1", "registry must be an object")
        registry = {}
    for key in ("schema_version","library","version","router","categories","skills"):
        if key not in registry: issue("V1", "missing top-level field: " + key)
    if type(registry.get("schema_version")) is not int or registry["schema_version"] != 1:
        issue("V1", "schema_version must be integer 1")
    if not isinstance(registry.get("library"), str) or not registry["library"].strip():
        issue("V1", "library must be nonempty")
    if not isinstance(registry.get("version"), str) or not SEMVER.fullmatch(registry["version"]):
        issue("V1", "invalid library version")
    check_path("V1", registry.get("router"))
    check_path("V6", "docs/INVARIANTS.md")
    cats = {}
    category_list = registry.get("categories")
    if not isinstance(category_list, list) or not category_list:
        issue("V1","categories must be a nonempty list")
        category_list = []
    for cat in category_list:
        if not isinstance(cat,dict) or not isinstance(cat.get("id"),str) or not string_list(cat.get("subcategories")):
            issue("V5","invalid category")
        elif cat["id"] in cats:
            issue("V5","duplicate category " + cat["id"])
        else:
            cats[cat["id"]] = cat["subcategories"]
    entries = registry.get("skills")
    if not isinstance(entries,list) or not entries:
        issue("V1","skills must be a nonempty list")
        entries = []
    commands = {}
    valid_dirs = {}
    for s in entries:
        if not isinstance(s,dict):
            issue("V2","skill entry must be object")
            continue
        k = s.get("id")
        missing = FIELDS - s.keys()
        if missing:
            issue("V2","missing fields: " + ", ".join(sorted(missing)), k)
        if not isinstance(k,str) or not ID.fullmatch(k) or k in skills:
            issue("V3","invalid or duplicate skill ID",k)
            continue
        skills[k] = s
        for f in ("name","description"):
            if not isinstance(s.get(f),str) or not s[f].strip(): issue("V2","invalid " + f,k)
        for f in ("triggers","tags","outputs","required_dependencies","optional_dependencies","platforms","references"):
            if not string_list(s.get(f)):
                issue("V2","invalid string list: " + f,k)
                s[f] = []
        caps = s.get("capabilities")
        if not isinstance(caps,dict) or not string_list(caps.get("preferred")) or not isinstance(caps.get("fallback"),str) or not caps["fallback"].strip():
            issue("V2","invalid capabilities",k)
        if not isinstance(s.get("adapters"),dict):
            issue("V2","invalid adapters",k)
            s["adapters"] = {}
        if not isinstance(s.get("version"),str) or not SEMVER.fullmatch(s["version"]) or s.get("status") not in ("active","draft","deprecated"):
            issue("V4","invalid skill version or status",k)
        category = s.get("category")
        if not isinstance(category,str) or category not in cats or s.get("subcategory") not in cats[category]:
            issue("V5","unknown category/subcategory",k)
        file = check_path("V6",s.get("path"),k)
        if file:
            if file.name != "SKILL.md":
                issue("V6","skill path must name SKILL.md",k,file)
            valid_dirs[k] = file.parent
            try:
                body = file.read_text(encoding="utf-8")
                meta = frontmatter(body)
                if meta.get("name") != k or not meta.get("description","").strip():
                    issue("V7","frontmatter name must match ID and description must be nonempty",k,file)
                count = len(body.split())
                counts[k] = count
                if count > maximum: issue("V8",f"Word count {count} exceeds max_skill_words ({maximum})",k,file)
                elif count > warning: issue("V8",f"Word count {count} exceeds warn_skill_words ({warning})",k,file,True)
            except (ValueError,OSError,UnicodeError) as exc:
                issue("V7",str(exc),k,file)
            if s.get("status") == "active":
                check_path("V6",str((file.parent/"evaluations/SCENARIOS.md").relative_to(root)),k)
        for value in s["references"] + list(s["adapters"].values()):
            target = check_path("V6",value,k)
            if file and target and not target.is_relative_to(file.parent):
                issue("V6","supporting file escapes skill directory",k,value)
        for platform in set(s["platforms"]) | set(s["adapters"]):
            if not ID.fullmatch(platform):
                issue("V13","invalid platform key",k)
            else:
                check_path("V13","platforms/"+platform+".md",k)
        if s.get("status") == "active":
            for token in s["triggers"]:
                if token.startswith(("@","/")):
                    token = token.lower()
                    if token in commands and commands[token] != k: issue("V14","duplicate command "+token,k)
                    commands[token] = k
    for k,s in skills.items():
        for dep in s["required_dependencies"] + s["optional_dependencies"]:
            if dep == k or dep not in skills: issue("V9","invalid dependency "+dep,k)
        for dep in s["required_dependencies"]:
            if s.get("status") == "active" and dep in skills and skills[dep].get("status") != "active":
                issue("V10","required dependency not active: "+dep,k)
    try:
        dependency_order(skills,skills)
        dependency_order(skills,skills,optional=True)
    except ValueError as exc:
        issue("V11",str(exc))
    for k,d in valid_dirs.items():
        for md in d.rglob("*.md"):
            if not md.resolve().is_relative_to(d):
                issue("V12","Markdown symlink escapes package",k,md)
                continue
            try:
                body = md.read_text(encoding="utf-8")
            except (OSError,UnicodeError) as exc:
                issue("V12",str(exc),k,md)
                continue
            for target in re.findall(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)",body):
                target = target.split("#",1)[0]
                if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",target): continue
                if target.startswith("../") or target.startswith("/") or "\\" in target:
                    issue("V12","unsafe relative link "+target,k,md)
                    continue
                resolved = (md.parent/target).resolve()
                if not resolved.is_relative_to(d) or not resolved.is_file():
                    issue("V12","broken or escaped relative link "+target,k,md)
    if trigger_file is not None:
        try:
            data = json.loads(trigger_file.read_text(encoding="utf-8"))
            if not isinstance(data,dict) or data.get("schema_version") != 1 or data.get("library") != registry.get("library") or not isinstance(data.get("cases"),list) or len(data["cases"]) < 12:
                raise ValueError("invalid trigger suite schema")
            seen = set()
            for case in data["cases"]:
                if not isinstance(case,dict): raise ValueError("invalid trigger case")
                cid = case.get("id","")
                if not isinstance(cid,str) or not re.fullmatch(r"TRG-\d{3}",cid) or cid in seen:
                    raise ValueError("invalid or duplicate trigger case ID")
                seen.add(cid)
                category, mode, prompt = case.get("category"),case.get("expected_mode"),case.get("prompt")
                expected, forbidden = case.get("expected_skills"),case.get("forbidden_skills")
                if category not in CATEGORIES or mode not in MODES or not isinstance(prompt,str) or len(prompt)<3 or not string_list(expected) or not string_list(forbidden):
                    raise ValueError(cid+": invalid case fields")
                if (set(expected)|set(forbidden))-skills.keys() or set(expected)&set(forbidden):
                    raise ValueError(cid+": unknown or overlapping skill IDs")
                if category in ("explicit_command","alias","install_protocol"):
                    actual_mode, actual = deterministic_route(prompt,skills)
                    if actual_mode != mode or set(actual)!=set(expected) or set(actual)&set(forbidden):
                        issue("V14",cid+": expected "+str((mode,expected))+" got "+str((actual_mode,actual)))
                    if category=="install_protocol" and actual!=expected:
                        issue("V14",cid+": incorrect dependency install order")
        except (ValueError,KeyError,TypeError,OSError) as exc:
            issue("V14",str(exc))
    return {"status":"fail" if errors else "pass","registry_version":registry.get("version"),
            "skills_checked":len(entries),"active_skills":sum(s.get("status")=="active" for s in skills.values()),
            "word_counts":counts,"errors":errors,"warnings":warnings}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--registry",type=Path,default=Path("registry.json"))
    p.add_argument("--max-skill-words",type=int,default=800)
    p.add_argument("--warn-skill-words",type=int,default=750)
    p.add_argument("--strict",action="store_true")
    p.add_argument("--check-triggers",action="store_true")
    p.add_argument("--triggers-file",type=Path,default=Path("evaluations/triggers.json"))
    p.add_argument("--format",choices=("text","json"),default="text")
    args=p.parse_args()
    if not 0 < args.warn_skill_words <= args.max_skill_words:
        p.error("word limits must satisfy 0 < warning <= maximum")
    root=args.root.resolve()
    try:
        registry=json.loads((root/args.registry).read_text(encoding="utf-8"))
    except (OSError,ValueError) as exc:
        print(str(exc),file=sys.stderr)
        return 2
    result=validate(root,registry,args.max_skill_words,args.warn_skill_words,(root/args.triggers_file) if args.check_triggers else None)
    if args.strict and result["warnings"]: result["status"]="fail"
    if args.format=="json": print(json.dumps(result,indent=2))
    else:
        print(f'{result["status"].upper()}: {result["active_skills"]} active skills; {len(result["errors"])} errors, {len(result["warnings"])} warnings')
        for severity in ("errors","warnings"):
            for item in result[severity]: print(severity[:-1].upper(),item)
        for k,n in result["word_counts"].items(): print(f"{k}: {n} words")
    return int(result["status"]=="fail")


if __name__=="__main__":
    sys.exit(main())
