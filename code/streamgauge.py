# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy"]
# ///
"""StreamGauge and its baselines: online accuracy monitors for delayed-label streams."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from scipy.signal import lfilter


def stitched_halfwidth(m_eff, var, alpha: float, rng_width: float=1.0):
    """Stitched empirical-Bernstein half-width (Howard et al., 2021)."""
    raise NotImplementedError('released upon publication')


def hoeffding_halfwidth(m_eff, alpha: float, rng_width: float=1.0):
    """Range-only Hoeffding half-width: the variance-blind alternative."""
    raise NotImplementedError('released upon publication')


def eb_halfwidth(m_eff, var, alpha: float, lam_cap: float=0.5, bet: str='opt'):
    """Operational empirical-Bernstein plug-in half-width."""
    raise NotImplementedError('released upon publication')


def ewma(x: np.ndarray, lam: float) -> np.ndarray:
    """Normalised exponentially weighted mean, sum lam^(t-s) x_s / sum lam^(t-s)."""
    raise NotImplementedError('released upon publication')


def ewma_weighted(x: np.ndarray, w: np.ndarray, lam: float, w2=None):
    """Weighted EW mean, its effective sample size, and its EW variance."""
    raise NotImplementedError('released upon publication')


def reference_estimand(correct: np.ndarray, w_ref: int=2001) -> np.ndarray:
    """A retrospective centred-label reference, not the probability path itself."""
    raise NotImplementedError('released upon publication')


def maturity_index(delay: np.ndarray) -> np.ndarray:
    """Index at which item t's label becomes readable (len(delay) means never)."""
    raise NotImplementedError('released upon publication')


def scatter_at_maturity(values: np.ndarray, weights: np.ndarray, mat: np.ndarray, T: int):
    """Move (value, weight) from serving index to maturity index."""
    raise NotImplementedError('released upon publication')


@dataclass
class SGConfig:
    alpha: float = 0.05
    budget: float = 0.1
    w0: float = 0.25
    n_fixed: int = 2000
    pi_min: float = 0.01
    pi_span: float = 4.0
    m_min: float = 50.0
    rho_mode: str = 'upper'
    rho_safety: float = 0.46
    delay_factor: float = 1.0
    centre_mode: str = 'track'
    centre_beta: float = 0.652
    clip_abstain: bool = True
    transport: bool = True
    restart_at: tuple[int, ...] = ()
    n_segments: int = 1
    mat_mode: str = 'none'
    mat_phi: tuple = ()
    mat_lag: int = 10000
    strat_ratio: float = 1.0
    strat_ref: int = 2000
    var_mode: str = 'iid'
    lrv_lags: int = 10
    lrv_window: int = 400
    tau_override: tuple[float, float] | None = None
    staleness_correction: bool = True
    forgetting: bool = True
    adaptive_lambda: bool = True
    ipw: bool = True
    anchor: bool = True
    variance_adaptive: bool = True
    eb_bet: str = 'opt'
    combine: str = 'select'
    label_only_fallback: bool = True
    spend_policy: str = 'uniform'
    n_grid: tuple[int, ...] = (250, 500, 1000, 2000, 4000, 8000)
    n_grid_g: tuple[int, ...] = (250, 500, 1000, 2000, 4000)
    d_min: int = 0
    rho_declared: float | None = None
    escalation: bool = False
    esc_budget: float = 0.01
    esc_burst: int = 400
    esc_delay: int = 25
    esc_window: int = 800


@dataclass
class Trace:
    est: np.ndarray
    lo: np.ndarray
    hi: np.ndarray
    abstain: np.ndarray
    spend: float
    rho: np.ndarray = field(default_factory=lambda: np.zeros(0))
    delta: np.ndarray = field(default_factory=lambda: np.zeros(0))
    n_bar: np.ndarray = field(default_factory=lambda: np.zeros(0))
    esc_spend: float = 0.0
    half_ppi: np.ndarray = field(default_factory=lambda: np.zeros(0))
    half_lab: np.ndarray = field(default_factory=lambda: np.zeros(0))
    used_lab: np.ndarray = field(default_factory=lambda: np.zeros(0, bool))
    msq: np.ndarray = field(default_factory=lambda: np.zeros(0))
    varlab: np.ndarray = field(default_factory=lambda: np.zeros(0))
    floor: float = 0.0
    wasted_labels: int = 0
    tau_g: float = 1.0
    tau_r: float = 1.0
    bought: np.ndarray = field(default_factory=lambda: np.zeros(0, bool))
    pi_used: np.ndarray = field(default_factory=lambda: np.zeros(0))

    @property
    def width(self) -> np.ndarray:
        raise NotImplementedError('released upon publication')


def run_streamgauge(signal: np.ndarray, correct: np.ndarray, delay: np.ndarray, cfg: SGConfig, seed: int=0, strat_score: np.ndarray | None=None) -> Trace:
    """Replay one stream and return the interval trace."""
    raise NotImplementedError('released upon publication')


def bl_label_free(score: np.ndarray, n_win: int) -> Trace:
    """Any monitor whose estimate is an exponentially weighted per-item score."""
    raise NotImplementedError('released upon publication')


def bl_prequential(correct: np.ndarray, delay: np.ndarray, n_win: int, alpha: float=0.05) -> Trace:
    """Prequential evaluation with delayed labels: honest, complete, and late."""
    raise NotImplementedError('released upon publication')


def bl_naive_seq_ppi(signal: np.ndarray, correct: np.ndarray, delay: np.ndarray, buy: np.ndarray, pi: np.ndarray, alpha: float=0.05) -> Trace:
    """Sequential PPI applied as though the estimand were fixed."""
    raise NotImplementedError('released upon publication')


def bl_discounted_labels(correct: np.ndarray, delay: np.ndarray, buy: np.ndarray, pi: np.ndarray, n_win: int, alpha: float=0.05) -> Trace:
    """Discounted-label empirical-Bernstein plug-in baseline."""
    raise NotImplementedError('released upon publication')


def bl_oracle(correct: np.ndarray, n_win: int) -> Trace:
    """Prequential evaluation with immediate labels, at a fixed window."""
    raise NotImplementedError('released upon publication')


def score(tr: Trace, truth: np.ndarray, burn_in: int=5000) -> dict:
    """Metrics against a supplied reference; validity depends on that reference."""
    raise NotImplementedError('released upon publication')


def recovery_steps(tr: Trace, cuts, horizon: int=8000) -> float:
    """Mean items from a known change point to the next certified reading."""
    raise NotImplementedError('released upon publication')


def demo() -> None:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    demo()
