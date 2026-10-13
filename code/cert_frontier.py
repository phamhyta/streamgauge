# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pandas", "pyarrow"]
# ///
"""How narrow could certified mode be, at best, and would a better radius help?"""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import pathlib
import numpy as np
import pandas as pd


OUT = pathlib.Path(__file__).resolve().parent.parent / 'results'
T = 8000
ALPHA = 0.05
K = 5
USEFUL_WIDTH = 0.25
V = 0.7 ** 2 * 0.75 * 0.25 + 0.01
PATHS = {'slow': 1.67e-05, 'smooth': 8.33e-05, 'ramp': 0.00025}
DECLARED = 1.05
BUDGETS = (0.1, 0.6)


def eb_radius(m, ell, v, cap=0.5):
    """The betting empirical-Bernstein radius, fixed-time optimal wager."""
    raise NotImplementedError('released upon publication')


def main() -> int:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    raise SystemExit(main())
