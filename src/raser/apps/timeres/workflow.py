"""Time-resolution setup resolution and dry-run plan."""

from __future__ import annotations

import json

from raser.apps._planning import WorkflowPlan
from raser.apps._planning import component_selection
from raser.apps.signal.workflow import build_plan as build_signal_plan
from raser.components import load_component
from raser.supports.paths import PACKAGE_ROOT


DEFAULT_G4SETUP = (
    PACKAGE_ROOT
    / "apps"
    / "timeres"
    / "components"
    / "g4setup"
    / "time_resolution.json"
)
DEFAULT_ADC = "Alibava"


def _load_g4setup():
    with DEFAULT_G4SETUP.open(encoding="utf-8") as stream:
        return DEFAULT_G4SETUP, json.load(stream)


def build_plan(kwargs) -> WorkflowPlan:
    g4setup = _load_g4setup()
    signal_plan = build_signal_plan(kwargs, g4setup=g4setup, workflow="timeres")
    adc_path, adc = load_component("adc", kwargs.get("adc") or DEFAULT_ADC)
    components = signal_plan.components + (component_selection("ADC", adc_path, adc),)
    return WorkflowPlan(
        workflow="timeres",
        device=signal_plan.device,
        field=signal_plan.field,
        components=components,
        stages=signal_plan.stages + ("ADC", "Metrics", "Time-resolution analysis"),
        output=signal_plan.output,
        work=signal_plan.work,
    )
