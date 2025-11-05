"""Python translation of ``Solver_Paper3.m``.

The script solves for the LCL filter elements (Lf, Lg, Cf) using the same set of
non-linear equations defined in the MATLAB version.  It relies on SciPy's
``fsolve`` routine to mirror the original workflow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy.optimize import fsolve

from root_Lf_L_Cf import root_Lf_L_Cf
from root_invL import root_invL


@dataclass
class FilterParameters:
    rb: float
    wripple: float
    tdd: float
    r: float

    @property
    def as_array(self) -> np.ndarray:
        return np.array([self.rb, self.wripple, self.tdd, self.r], dtype=float)


def solve_filter_components(
    params: FilterParameters,
    lf_initial: float,
    lg_initial: float,
    cf_initial: float,
    maxfev: int = 600,
    xtol: float = 1e-9,
) -> dict[str, float]:
    """Solve the coupled equations for the LCL filter components.

    Returns a dictionary that mirrors the MATLAB script output.
    """
    l_initial = lf_initial + lg_initial
    x0 = np.array([lf_initial, l_initial, cf_initial], dtype=float)

    solution = fsolve(
        lambda x: root_Lf_L_Cf(x, params.as_array),
        x0,
        xtol=xtol,
        maxfev=maxfev,
    )

    lf, l_total, cf = solution
    lg = l_total - lf

    inv_solution = fsolve(
        lambda y: root_invL(y, params.as_array),
        l_initial,
        xtol=xtol,
        maxfev=maxfev,
    )
    inv_root = float(inv_solution[0])

    lf2 = params.r / inv_root
    lg2 = 1.0 / inv_root - lf2
    cf2 = (1.0 / inv_root) / params.rb**2

    return {
        "Lf": lf,
        "Lg": lg,
        "Cf": cf,
        "Lf2": lf2,
        "Lg2": lg2,
        "Cf2": cf2,
    }


def main() -> None:
    params = FilterParameters(
        rb=1.613,
        wripple=2 * np.pi * 10e3,
        tdd=5.0,
        r=0.75,
    )

    results = solve_filter_components(
        params=params,
        lf_initial=81.5e-6 / 3.0,
        lg_initial=27.2e-6 / 3.0,
        cf_initial=41.8e-6 / 3.0,
    )

    for key, value in results.items():
        print(f"{key} = {value:.6e}")


if __name__ == "__main__":
    main()
