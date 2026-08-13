"""Interpolation and potential-gradient calculations for Field data."""

from __future__ import annotations

from typing import Any, Callable, Mapping, Sequence

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.interpolate import griddata
from scipy.interpolate import interp1d


def interpolate_1d(data: Mapping[str, Any]):
    return interp1d(data["points"], data["values"])


def interpolate_2d(data: Mapping[str, Any]):
    points = np.asarray(data["points"], dtype=np.float64)
    values = np.asarray(data["values"], dtype=np.float64)
    return lambda x, y: float(griddata(points, values, (x, y), method="linear"))


def interpolate_3d(data: Mapping[str, Any]):
    points = np.asarray(data["points"], dtype=np.float64)
    values = np.asarray(data["values"], dtype=np.float64)
    axes = tuple(np.unique(points[:, axis]) for axis in range(3))
    expected = np.prod([len(axis) for axis in axes])
    if len(points) != expected:
        return lambda x, y, z: float(
            griddata(points, values, (x, y, z), method="linear", fill_value=0.0)
        )
    indices = tuple(np.searchsorted(axes[axis], points[:, axis]) for axis in range(3))
    grid = np.empty(tuple(len(axis) for axis in axes), dtype=np.float64)
    grid[indices] = values
    interpolator = RegularGridInterpolator(
        axes,
        grid,
        method="linear",
        bounds_error=True,
    )
    return lambda x, y, z: float(interpolator((x, y, z)))


def calculate_gradient(
    function: Callable[..., float],
    coordinates: Sequence[float],
    *,
    step: float = 1.0e-5,
) -> tuple[float, ...]:
    if step <= 0:
        raise ValueError("Gradient step must be positive")
    point = tuple(map(float, coordinates))
    gradient = []
    for axis in range(len(point)):
        upper = list(point)
        lower = list(point)
        upper[axis] += step / 2.0
        lower[axis] -= step / 2.0
        gradient.append((float(function(*upper)) - float(function(*lower))) / step)
    return tuple(gradient)
