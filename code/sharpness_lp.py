# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy", "pandas", "pyarrow"]
# ///
"""Is the identified half-width of thm:sharp attained, or merely an upper bound?"""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import pathlib
import sys
import numpy as np
import pandas as pd
from scipy.optimize import linprog


OUT = pathlib.Path(__file__).resolve().parent.parent / 'results'
TOL = 1e-07


def modulus(kind: str, rho: float, cap: float=0.12):
    """v(d), nondecreasing with v(0)=0."""
    raise NotImplementedError('released upon publication')


def cost_matrix(v, ages: np.ndarray, clip_at: np.ndarray | None=None):
    """v(|a-b|), optionally truncated at the distance to the [0,1] boundary."""
    raise NotImplementedError('released upon publication')


def transport_primal(p: np.ndarray, q: np.ndarray, c: np.ndarray) -> float:
    """min <Gamma, c> over couplings with marginals p, q."""
    raise NotImplementedError('released upon publication')


def witness_path(p: np.ndarray, q: np.ndarray, c: np.ndarray, box: tuple[float, float] | None=None):
    """max sum (p-q) g over paths with |g_a - g_b| <= c[a,b]."""
    raise NotImplementedError('released upon publication')


def tracking_term(q: np.ndarray, ages: np.ndarray, v) -> tuple[float, float]:
    """T_v(Q, delta_0) in closed form, and by the same witness LP."""
    raise NotImplementedError('released upon publication')


def real_age_laws(n_pairs: int=6, max_age: int=40):
    """(P, Q) age histograms taken from an actual monitor run."""
    raise NotImplementedError('released upon publication')


def synthetic_age_laws(rng, n_pairs: int=6, max_age: int=40):
    raise NotImplementedError('released upon publication')


def main() -> int:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    raise SystemExit(main())
