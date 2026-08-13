"""Sensor electrical modelling and analog front-end circuit assembly."""

from .network import CurrentSource
from .network import FrontendCircuit
from .network import FrontendWaveforms
from .network import assemble_frontend
from .network import solve_frontend

__all__ = [
    "CurrentSource",
    "FrontendCircuit",
    "FrontendWaveforms",
    "assemble_frontend",
    "solve_frontend",
]


def trans(name):
    from .legacy import trans as legacy_trans

    return legacy_trans(name)


def readout(name):
    from .legacy import readout as legacy_readout

    return legacy_readout(name)
