# Project command

_RASER 5.0 project creation in `src/raser/cli/project.py`_

---

## 📋 Responsibility

`raser project` creates an application project beneath the work root and may
populate it from an application template. Reusable-object projects, including
Device projects, follow the separate ownership model defined in
[Architecture](../architecture.md).

## ⌨️ Command

```bash
raser project create my-study
raser project create my-study --template signal
```

The first form initializes an empty component namespace. A template adds
[Components](../components/README.md) and configuration owned by the selected
application. CCE and time-resolution templates include Signal inputs because
those workflows compose Signal.

## 🗂️ Result

```text
work/my-study/
└── components/
```

Template-specific input files retain the relative layout expected by the
application. A Device component references a Device project, where the
Device definition and Field data remain. The owning workflow later creates
generated runs outside `components/`.

The work root and active path semantics are defined by
[Supports paths](../supports/paths.md).

## ⚠️ Failure contract

Project names resolve beneath the work root. An existing destination raises a
conflict before any merge or overwrite. Unknown templates, missing template
assets, invalid names, copy failures, and filesystem errors return a failed
creation result.
