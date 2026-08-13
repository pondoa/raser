"""TCT component resolution and dry-run plan."""

from __future__ import annotations

from pathlib import Path

from raser.apps._planning import WorkflowPlan
from raser.apps._planning import component_selection
from raser.components import load_component
from raser.components import load_laser
from raser.core.device import resolve_device
from raser.core.field import FieldConfiguration
from raser.supports.paths import project_path


DEFAULT_AFE = "Broad_Band_UCSC"


def build_plan(kwargs) -> WorkflowPlan:
    state = {}
    if kwargs.get("voltage") is not None:
        state["bias_voltage"] = float(kwargs["voltage"])
    device = resolve_device(kwargs["det_name"], state=state)
    field = FieldConfiguration.from_device(device)
    laser_path, laser = load_laser(kwargs["laser"])
    afe_path, afe = load_component("afe", kwargs.get("amplifier") or DEFAULT_AFE)
    if not device.definition.electrical:
        raise ValueError(
            f"Device {device.name} requires electrical values for Frontend"
        )

    mode = kwargs.get("tct_mode") or "signal"
    stages = ["Interaction", "Current", "Frontend"]
    if mode.startswith("position"):
        stages.append("Position analysis")
    return WorkflowPlan(
        workflow="tct",
        device=device.as_dict(),
        field={
            "configuration": field.as_dict(),
            "hash": field.digest,
            "directory": str(field.directory(device)),
        },
        components=(
            component_selection("Laser", laser_path, laser),
            component_selection("AFE", afe_path, afe),
        ),
        stages=tuple(stages),
        output=Path(project_path("tct")),
        work={
            "jobs": int(kwargs.get("scan") or 1),
            "seed": int(kwargs.get("seed") or 0),
        },
    )
