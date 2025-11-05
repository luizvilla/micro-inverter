"""Scalar equation used to size inverter inductances.

This is a direct translation of the MATLAB ``root_invL`` helper that is
referenced by ``Solver_Paper3.m``.  It is kept numerically identical so that
the Python solver can reuse the same residual function.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def root_invL(x: ArrayLike, param: ArrayLike):
    """Return the residual of the cubic equation defined in ``root_invL.m``.

    Parameters
    ----------
    x:
        Unknown (scalar) variable.  When called from ``scipy.optimize.fsolve``,
        this will typically be a NumPy array of shape ``(1,)``.
    param:
        Iterable containing ``[Rb, wripple, TDD, r]``.
    """
    scalar_input = np.isscalar(x)
    x_arr = np.atleast_1d(np.asarray(x, dtype=float))
    rb, wripple, tdd, r = np.asarray(param, dtype=float)

    value = (
        x_arr**3
        + (wripple * tdd) / (50.0 * rb) * x_arr**2
        - r * (1.0 - r) * tdd * (wripple**3) / (50.0 * rb**3)
    )

    if scalar_input:
        return float(value.item())
    return value


__all__ = ["root_invL"]
