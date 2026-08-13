# Command-line interface

_RASER 5.0 installed entry point under `src/raser/cli/`_

The supported entry point is `raser`. User instructions use this installed
command; source-tree module invocations remain implementation details.

---

## ⌨️ Command surface

```bash
raser --help
raser <command> --help
```

| Public command | Owning package |
| --- | --- |
| `bmos` | [`apps/bmos`](../apps/bmos.md) |
| `cce` | [`apps/cce`](../apps/cce.md) |
| `field` | [Core Field](../core/field.md) |
| `lumi` | [`apps/lumi`](../apps/lumi.md) |
| `project` | [`cli/project.py`](project.md) |
| `signal` | [`apps/signal`](../apps/signal.md) |
| `tct` | [`apps/tct`](../apps/tct.md) |
| `telescope` | [`apps/telescope`](../apps/telescope.md) |
| `timeres` | [`apps/timeres`](../apps/timeres.md) |

Direct implementation capabilities are grouped under `raser dev`:

| Developer command | Core package |
| --- | --- |
| `frontend` | [Frontend](../core/frontend.md) |
| `control` | [Control draft](../core/draft/control.md) |
| `current` | [Current](../core/current.md) |
| `adc` | [ADC draft](../core/draft/adc.md) |
| `field` | [Field](../core/field.md) |
| `interaction` | [Interaction](../core/interaction.md) |
| `metrics` | [Metrics](../core/metrics.md) |

CLI help is the authoritative syntax and option reference. Unregistered
top-level forms fail explicitly.

## 🔀 Routing

[`raser.py`](raser.md) owns parsing, route descriptors, lazy import, temporary
project/component context, process exit status, global batch dispatch, and
runtime cleanup. Applications receive the parsed top-level argument values
from the router.

Each route declares at most one project selector. Project inference and
component lookup follow [Supports paths](../supports/paths.md).

## ⚙️ Batch boundaries

Global `raser -b <command>` submits one complete command. An application's
indexed mode expands one recorded run into workers. These are separate parser
and ownership boundaries; see [Jobs](../supports/jobs.md) and
[Runs](../supports/runs.md).
