# Invocation and optional installation

## ChatGPT Chat / Work

Invoke using the README prompt. With authorized repository access, the assistant retrieves ROUTER.md, registry.json and matching skill files at runtime. This does not create a persistent skill or grant tools. If retrieval is unavailable, attach the necessary files or paste them. In a reusable project, the invocation instruction can be saved as project guidance if the interface supports it.

## Gemini Chat / Task

The same dynamic invocation works when repository retrieval is available. If the user explicitly wants to install a skill and the current interface offers native skills, choose the specific skill, review its SKILL.md and supporting files, and use the available native import/create mechanism. If the interface requires a package or different format, adapt the chosen skill to that format without changing the canonical repository. Never silently install or generate a native skill. No native installation is necessary for dynamic invocation.

For Delegate, use the canonical skill and the Gemini Task adapter if native sub-agent tools are exposed. Include audit-contract.md if the installation supports supporting files. If the host cannot resolve repository-relative references, provide the required reference content with the installation.

For Ask, use the canonical skill and the Gemini Task adapter if a native structured multiple-choice question tool is exposed; otherwise rely on the portable Markdown fallback.

For Animate, make the canonical skill, its references and the required Delegate skill available; also include 3D for three-dimensional animation. Install only on explicit user request. If the host cannot resolve dependencies, retrieve or provide their instructions and use the documented capability fallback.

Feature availability and UI vary by plan, host and rollout; this repository does not guarantee a specific install button or tool interface.

For Max, include its goal audit contract, required Delegate instructions and applicable adapters; use the bounded sequential fallback when native independent workers are unavailable. For Review, include Delegate and the rubric/dashboard references, preserving read-only source authorization. For MSDeck, include its navigation, media and verification references; include 3D, Animate or Delegate only when selected (Animate requires Delegate). Missing essential supporting instructions must be retrieved or disclosed; native installation remains optional and explicitly user-controlled.
