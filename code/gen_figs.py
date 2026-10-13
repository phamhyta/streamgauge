# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "matplotlib", "seaborn", "pandas", "pyarrow",
#                 "scipy", "scikit-learn"]
# ///
"""Render every experiment figure from the measured results in results/."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import pathlib
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / 'results'
OUT = ROOT / 'latex' / 'figures'


def save(fig, name):
    raise NotImplementedError('released upon publication')


def read(block: str) -> pd.DataFrame | None:
    raise NotImplementedError('released upon publication')


def ci(x, cluster=None) -> float:
    """Bootstrap streams when supplied; otherwise use within-stream draws."""
    raise NotImplementedError('released upon publication')


def fig_pareto():
    """Tracking error against label spend: the three information regimes."""
    raise NotImplementedError('released upon publication')


def fig_coverage():
    """Local surrogate coverage through one stream, smoothed over position."""
    raise NotImplementedError('released upon publication')


def fig_calibration():
    """(a) empirical vs nominal coverage; (b) what the width target selects."""
    raise NotImplementedError('released upon publication')


def fig_feasibility():
    """Operational candidate-width ratios, averaged over time and seeds."""
    raise NotImplementedError('released upon publication')


def fig_frontier():
    """Budget x latency sensitivity as annotated heatmaps."""
    raise NotImplementedError('released upon publication')


ABL_SHORT = {'- fixed-time EB wager': '$-$ fixed-time EB', '- staleness correction': '$-$ staleness corr.', '- transport charge': '$-$ transport charge', '- forgetting window': '$-$ forgetting window', '- adaptive forgetting': '$-$ adaptive forget.', '- inverse-propensity weighting': '$-$ purchase IPW', '- variance-adaptive radius': '$-$ variance-adaptive', '- label-only fallback': '$-$ label-only fallback', '- decoupled centre': '$-$ decoupled centre', '- centre lag term': '$-$ centre lag term', '- anchor (signal layer only)': '$-$ anchor'}


def fig_ablation():
    """Signed deltas against the full method, around a zero baseline."""
    raise NotImplementedError('released upon publication')


def fig_spend():
    """Where each purchase policy lands on the coverage-width curve."""
    raise NotImplementedError('released upon publication')


FAM_SHORT = {'gbt': 'GBT', 'mlp': 'MLP', 'linear': 'Linear', 'uncal': 'Uncal.', 'llm-icl': 'LLM'}


def fig_generality():
    """Label-free error -> StreamGauge error, per predictor family."""
    raise NotImplementedError('released upon publication')


def fig_escalation():
    """Pool sensitivity per stream, with seed-bootstrap intervals per curve."""
    raise NotImplementedError('released upon publication')


def fig_efficiency():
    """Per-item update cost, decomposed by switching components off."""
    raise NotImplementedError('released upon publication')


def fig_episode():
    """The taxonomy-rename episode: truth, signal, delayed score, interval."""
    raise NotImplementedError('released upon publication')


def fig_intro2():
    """Two-panel teaser on a replayed injected-drift stream."""
    raise NotImplementedError('released upon publication')


def fig_certgain():
    """EXP-01: scheduled variance-adaptive radius vs label-only, known paths."""
    raise NotImplementedError('released upon publication')


FIGS = {'pareto': fig_pareto, 'coverage': fig_coverage, 'calibration': fig_calibration, 'feasibility': fig_feasibility, 'frontier': fig_frontier, 'ablation': fig_ablation, 'spend': fig_spend, 'generality': fig_generality, 'escalation': fig_escalation, 'efficiency': fig_efficiency, 'episode': fig_episode, 'intro2': fig_intro2, 'certgain': fig_certgain}


if __name__ == '__main__':
    raise NotImplementedError('released upon publication')
