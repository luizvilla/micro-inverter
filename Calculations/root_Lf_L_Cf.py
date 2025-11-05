"""Vector residual function matching ``root_Lf_L_Cf.m``.

The function exposes the same three non-linear equations that are solved in
``Solver_Paper3.m`` to compute the filter components (Lf, L, Cf).
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def root_Lf_L_Cf(x: ArrayLike, param: ArrayLike) -> np.ndarray:
    """Return the three residual equations from the MATLAB implementation.

    Parameters
    ----------
    x:
        Iterable with the unknowns ``[Lf, L, Cf]``.
    param:
        Iterable containing ``[Rb, wripple, TDD, r]``.
    """
    x_arr = np.asarray(x, dtype=float)
    if x_arr.shape != (3,):
        x_arr = np.reshape(x_arr, (3,))

    rb, wripple, tdd, r = np.asarray(param, dtype=float)
    lf, l_total, cf = x_arr

    eq1 = lf / l_total - r

    denominator = r * (1.0 - r) * l_total * cf
    eq2 = (1.0 / (r * (1.0 - r) * l_total**2 * cf)) / (
        wripple * (wripple**2 - 1.0 / denominator)
    ) - tdd / (50.0 * rb)

    eq3 = l_total / cf - rb**2

    return np.array([eq1, eq2, eq3], dtype=float)


__all__ = ["root_Lf_L_Cf"]
