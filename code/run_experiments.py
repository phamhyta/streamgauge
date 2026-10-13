# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy", "pandas", "scikit-learn", "pyarrow"]
# ///
"""Run every StreamGauge experiment and write measured results to results/."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import os
import pathlib
import sys
import time
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import pandas as pd
from baselines_query import bl_adwin_reset, bl_iupm_ui, bl_mldemon
from streamgauge import SGConfig, bl_discounted_labels, bl_label_free, bl_naive_seq_ppi, bl_oracle, bl_prequential, maturity_index, recovery_steps, reference_estimand, run_streamgauge, score
from streams import ALL_SPECS, CACHE, IMAGE_SPECS, MAX_LEN, MODELS, SPECS, TEXT_SPECS, build, model_applies


RES = pathlib.Path(__file__).resolve().parent.parent / 'results'
SEEDS = list(range(10))
E_DELAYS = [50, 200, 500, 2000]
DEFAULT_DELAY = 500
BUDGET = 0.1
N_WIN = 2000
BURN = 5000
WORKERS = int(os.environ.get('SG_WORKERS', max(1, (os.cpu_count() or 4) - 2)))


def available(names, model: str='gbt') -> list:
    """Streams whose frozen-predictor cache is on this machine."""
    raise NotImplementedError('released upon publication')


def draw_delay(T: int, mean_d: float, seed: int, correct=None, label_dependent: bool=False) -> np.ndarray:
    """Log-normal verification latency; optionally label-dependent."""
    raise NotImplementedError('released upon publication')


def purchase(T: int, budget: float, seed: int):
    raise NotImplementedError('released upon publication')


_CACHE: dict = {}


def load(name: str, model: str='gbt'):
    """Stream plus its retrospective reference, memoised per worker process."""
    raise NotImplementedError('released upon publication')


def sg(name, d, truth, seed, mean_d, cfg_kw=None, label_dep=False):
    raise NotImplementedError('released upon publication')


def declared_rho(truth: np.ndarray, h: int=2000) -> float:
    """Retrospective lag-slope setting for the operational triage diagnostic."""
    raise NotImplementedError('released upon publication')


def modality(name: str) -> str:
    raise NotImplementedError('released upon publication')


def change_points(d, T: int) -> list:
    """Injected change points in *monitored* coordinates."""
    raise NotImplementedError('released upon publication')


def rq1() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq2() -> pd.DataFrame:
    """Local surrogate coverage through the stream, averaged over seeds."""
    raise NotImplementedError('released upon publication')


FR_DELAYS = [50, 100, 200, 500, 1000, 2000, 5000]
FR_BUDGETS = [0.02, 0.1, 0.5]


def rq3() -> pd.DataFrame:
    """The budget x latency grid, on every stream."""
    raise NotImplementedError('released upon publication')


ABLATIONS = {'StreamGauge (full)': {}, '- staleness correction': dict(staleness_correction=False), '- forgetting window': dict(forgetting=False), '- adaptive forgetting': dict(adaptive_lambda=False), '- inverse-propensity weighting': dict(ipw=False), '- variance-adaptive radius': dict(variance_adaptive=False), '- label-only fallback': dict(label_only_fallback=False), '- transport charge': dict(transport=False), '- fixed-time EB wager': dict(eb_bet='pm'), '- decoupled centre': dict(centre_mode='midpoint'), '- centre lag term': dict(centre_beta=0.0), '- anchor (signal layer only)': dict(anchor=False)}


def rq4() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


WINDOWS = (250, 500, 1000, 2000, 4000, 8000)


def rq_window() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq5() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq6() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq6_slices() -> pd.DataFrame:
    """Per-slice monitoring with a Bonferroni-adjusted level."""
    raise NotImplementedError('released upon publication')


PQ_REF_US = 0.329
LF_REF_US = 0.097


def rq7() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq7_cost() -> pd.DataFrame:
    """What each part of the construction costs, by switching it off."""
    raise NotImplementedError('released upon publication')


def rq8() -> pd.DataFrame:
    """Does the monitor survive changing the predictor family and modality?"""
    raise NotImplementedError('released upon publication')


def rq9() -> pd.DataFrame:
    """Sweep the expedited-label pool and the width target jointly."""
    raise NotImplementedError('released upon publication')


POOL_SWEEP = (0.0, 0.02, 0.05, 0.1, 0.2)


def rq9_pool() -> pd.DataFrame:
    """Sweep the expedited pool past the declared operating point."""
    raise NotImplementedError('released upon publication')


RECOVERY_SEEDS = list(range(40))


def rq9_recovery() -> pd.DataFrame:
    """Recovery time after a change, at enough seeds to say something."""
    raise NotImplementedError('released upon publication')


def rq_cal_alpha() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


W0_SWEEP = (0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.6, 1.0)


def rq_cal_w0() -> pd.DataFrame:
    """The selection effect of the usefulness target."""
    raise NotImplementedError('released upon publication')


FEAS_LAMBDAS = (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.0)


def rq_feasibility() -> pd.DataFrame:
    """Sweep signal quality and record which certificate wins."""
    raise NotImplementedError('released upon publication')


def rq_triage() -> pd.DataFrame:
    """Is an abstention unanswerable, or a deficit that labels can fix?"""
    raise NotImplementedError('released upon publication')


INSTANT_STREAMS = ['electricity', 'airlines', 'creditcard', 'huffpost-taxonomy']


def rq_instant() -> pd.DataFrame:
    """Labels arrive the moment they are requested, total spend matched."""
    raise NotImplementedError('released upon publication')


def rq_episode() -> pd.DataFrame:
    """One drift episode on the natural relabelling arm, quarter by quarter."""
    raise NotImplementedError('released upon publication')


CERT_T = 8000


def rq_certified() -> pd.DataFrame:
    """The one experiment the surrogate cannot do: test thm:cs itself."""
    raise NotImplementedError('released upon publication')


def rq_regime() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq_delayshape() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


ETA_GRID = (0.1, 0.16, 0.22, 0.3, 0.38, 0.46, 0.54, 0.66, 0.8, 1.0, 1.3)


def rq_eta() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


WR_WINDOWS = (400, 500, 600, 700, 800, 900, 1000, 1400, 2000)
WR_DELAYS = (50, 500, 2000)


def rq_window_regime() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


WREF_SWEEP = (501, 1001, 2001, 4001, 8001)


def rq_score_sens() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


RHO_MODES = ('debias', 'upper', 'envelope')
RHO_ETAS = (0.2, 0.3, 0.46, 0.7, 1.1, 1.6, 2.4)


def rq_rho() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq_stationary() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq_coupled() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq_bltune() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


SCAL_WINDOWS = (250, 500, 1000, 2000, 4000, 8000, 16000, 32000)
SCAL_BUDGETS = (0.02, 0.05, 0.1, 0.25, 0.5)


def rq_scaling() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


SER_PHI = (0.0, 0.5, 0.8, 0.9, 0.95, 0.99)


def rq_serial() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


CS_T = 16000
CS_WINDOWS = (200, 283, 400, 566, 800, 1131, 1600, 2263, 3200, 4525, 6400)
CS_BUDGETS = (0.02, 0.05, 0.1, 0.25, 0.5)


def rq_certscale() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


def rq_knownpath() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


HZN_T = 200000
HZN_NMAX = (800, 1131, 1600, 2263, 3200)
HZN_LOOKS = (8, 25, 80, 250, 800, 2500)
HZN_GROWTH_T0 = 20000


def rq_horizon() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


UPD_STREAMS = ('insects-abrupt', 'insects-gradual', 'electricity', 'airlines', 'covertype', 'huffpost-taxonomy', 'huffpost-topic')
UPD_PAIRS = (('gbt', 'mlp'), ('mlp', 'gbt'), ('gbt', 'linear'), ('linear', 'gbt'), ('mlp', 'linear'), ('linear', 'mlp'))
UPD_T0 = (18000, 24000)
UPD_PRE = 13000
UPD_SHAM = 6000


def rq_update() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


LRV_PHI = (0.0, 0.8, 0.95, 0.99, 0.995, 0.998)
LRV_MODES = ('iid', 'block', 'oracle', 'marg')


def rq_lrv() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


JOINT_R = (1.0, 3.0, 9.0)


def rq_joint() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


CG_T = 100000
CG_LOOKS = tuple((10000 * l - 1 for l in range(1, 11)))
CG_DELAY = 200
CG_ALPHA = 0.05
CG_SLOW_PERIOD = 400000
CG_FLIP = 0.3
CG_SHIFT = 0.15
CG_CONST = 0.8
CG_LONG = (5000, 20000, 50000, 100000)
CG_SHORT = (250, 500, 1000, 2000)
CG_SIGNALS = ('ideal', 'strong', 'moderate', 'miscal', 'constant')
CG_COVERAGE = {('strong', 'stationary', 'honest', 0.1, 'flat', 'aligned'), ('strong', 'drift', 'honest', 0.1, 'flat', 'aligned'), ('strong', 'slowdrift', 'honest', 0.1, 'flat', 'aligned'), ('strong', 'drift', 'misdeclared', 0.1, 'flat', 'aligned'), ('ideal', 'drift', 'honest', 0.1, 'flat', 'aligned'), ('moderate', 'stationary', 'honest', 0.1, 'flat', 'aligned')}


def rq_certgain() -> pd.DataFrame:
    raise NotImplementedError('released upon publication')


BLOCKS = {'rq1': rq1, 'rq2': rq2, 'rq3': rq3, 'rq4': rq4, 'rq5': rq5, 'rq6': rq6, 'rq6_slices': rq6_slices, 'rq7': rq7, 'rq7_cost': rq7_cost, 'rq8': rq8, 'rq9': rq9, 'rq9_recovery': rq9_recovery, 'rq9_pool': rq9_pool, 'rq_cal_alpha': rq_cal_alpha, 'rq_cal_w0': rq_cal_w0, 'rq_feasibility': rq_feasibility, 'rq_triage': rq_triage, 'rq_instant': rq_instant, 'rq_episode': rq_episode, 'rq_certified': rq_certified, 'rq_window': rq_window, 'rq_regime': rq_regime, 'rq_delayshape': rq_delayshape, 'rq_eta': rq_eta, 'rq_window_regime': rq_window_regime, 'rq_score_sens': rq_score_sens, 'rq_rho': rq_rho, 'rq_stationary': rq_stationary, 'rq_coupled': rq_coupled, 'rq_bltune': rq_bltune, 'rq_scaling': rq_scaling, 'rq_knownpath': rq_knownpath, 'rq_certscale': rq_certscale, 'rq_serial': rq_serial, 'rq_horizon': rq_horizon, 'rq_update': rq_update, 'rq_lrv': rq_lrv, 'rq_joint': rq_joint, 'rq_certgain': rq_certgain}


if __name__ == '__main__':
    raise NotImplementedError('released upon publication')
