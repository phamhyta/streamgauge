# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""Active-querying monitors for the zero-latency limit."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import numpy as np
from streamgauge import Trace, eb_halfwidth, ewma, maturity_index, scatter_at_maturity


class _Budget:
    """Multiplicative gain holding the realised query rate at `budget`."""

    def __init__(self, budget: float):
        raise NotImplementedError('released upon publication')

    def rate(self, t: int, boost: float, lo: float=0.002) -> float:
        raise NotImplementedError('released upon publication')

    def took(self) -> None:
        raise NotImplementedError('released upon publication')


def bl_adwin_reset(correct: np.ndarray, delay: np.ndarray, buy: np.ndarray, pi: np.ndarray, delta: float=0.002, min_seg: int=200) -> Trace:
    """Prequential scoring with an ADWIN-style adaptive window over matured labels."""
    raise NotImplementedError('released upon publication')


def bl_mldemon(signal: np.ndarray, correct: np.ndarray, budget: float=0.1, n_win: int=2000, alpha: float=0.05, tol: float=0.125, delta_rate: float=0.0002, z_thresh: float=3.0, seed: int=0) -> Trace:
    """MLDemon-style monitoring: coast on the unlabeled stream, query on doubt."""
    raise NotImplementedError('released upon publication')


def bl_iupm_ui(signal: np.ndarray, correct: np.ndarray, margin: np.ndarray, budget: float=0.1, n_win: int=2000, seed: int=0) -> Trace:
    """IUPM-style uncertainty-driven monitoring with active labeling."""
    raise NotImplementedError('released upon publication')


def demo() -> None:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    demo()
