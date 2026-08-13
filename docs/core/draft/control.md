# Control models

_RASER 5.0 reusable control logic under `src/raser/core/control/`_

---

## 📋 Responsibility

Core Control contains reusable control-logic models and their simulation
harnesses. Applications supply workflow, DAQ policy, project layout, and analog
readout configuration.

## ⚙️ Registered incrementer

`RegIncr` defines an 8-bit input/output port contract with clocked register
behavior. `regincr_sim` drives explicit vectors, advances the model by declared
cycles, and emits developer diagnostics and VCD traces under a caller-owned
output path.

## 🔗 Boundary

Direct developer execution is available through `raser dev control
regincr_sim`. An application must define an explicit mixed-signal or DAQ
handoff before a Control model participates in a scientific workflow.

## ⚠️ Failure contract

Invalid port widths, malformed vectors, unsupported cycles, PyMTL translation
failures, and output errors propagate. Simulation accepts values satisfying the
declared port contract.
