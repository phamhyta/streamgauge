# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""Reference implementation of the certified transport confidence tube."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from scipy.stats import wasserstein_distance


@dataclass(frozen=True)
class CertifiedConfig:
    alpha: float = 0.05
    budget: float = 0.1
    rho_theta: float = 0.0001
    rho_signal: float = 0.0001
    signal_windows: tuple[int, ...] = (250, 500, 1000, 2000)
    anchor_windows: tuple[int, ...] = (500, 1000, 2000, 4000)
    min_anchor: int = 20
    useful_width: float = 0.25
    horizon: int | None = None
    looks: tuple[int, ...] = ()
    growth: str = 'fixed'
    growth_t0: int = 1000


@dataclass
class CertifiedTrace:
    est: np.ndarray
    lo: np.ndarray
    hi: np.ndarray
    abstain: np.ndarray
    signal_choice: np.ndarray
    anchor_choice: np.ndarray
    noise: np.ndarray
    signal_transport: np.ndarray
    target_transport: np.ndarray
    purchased: np.ndarray
    look: np.ndarray = field(default_factory=lambda: np.zeros(0, dtype=bool))
    bridge: np.ndarray = field(default_factory=lambda: np.zeros(0))
    anchor_count: np.ndarray = field(default_factory=lambda: np.zeros(0, dtype=int))

    @property
    def width(self) -> np.ndarray:
        raise NotImplementedError('released upon publication')


def run_certified(signal: np.ndarray, correct: np.ndarray, delay: np.ndarray, cfg: CertifiedConfig, seed: int=0) -> CertifiedTrace:
    """Run the finite-grid certified monitor."""
    raise NotImplementedError('released upon publication')


def demo() -> None:
    raise NotImplementedError('released upon publication')


@dataclass(frozen=True)
class ScheduledVRConfig:
    alpha: float = 0.05
    looks: tuple[int, ...] = ()
    signal_kernels: tuple[tuple[str, float], ...] = (('box', 10000),)
    anchor_kernels: tuple[tuple[str, float], ...] = (('box', 10000),)
    rho_theta: float = 0.0
    rho_signal: float = 0.0
    min_anchor: int = 20


def vr_look(t: int, signal: np.ndarray, correct: np.ndarray, obs_idx: np.ndarray, cfg: ScheduledVRConfig) -> dict:
    """All candidate radii of thm:vr and the label-only Bernstein family at t."""
    raise NotImplementedError('released upon publication')


def run_scheduled_vr(signal: np.ndarray, correct: np.ndarray, delay: np.ndarray, purchased: np.ndarray, cfg: ScheduledVRConfig) -> dict:
    """Scheduled VR / label-only monitor on one stream (EXP-01)."""
    raise NotImplementedError('released upon publication')


def vr_selfcheck() -> None:
    """Arithmetic and boundary regression checks for the scheduled VR path."""
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    demo()
