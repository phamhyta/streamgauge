# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pandas", "pyarrow", "scipy", "scikit-learn"]
# ///
"""Render every LaTeX table from the measured results in results/."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import pathlib
import json
import sys
import numpy as np
import pandas as pd


ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / 'results'
TAB = ROOT / 'latex' / 'tables'
STREAM_TEX = {'insects-abrupt': '\\textsc{Insects}-abrupt', 'insects-gradual': '\\textsc{Insects}-gradual', 'electricity': '\\textsc{Electricity}', 'airlines': '\\textsc{Airlines}', 'covertype': '\\textsc{Covertype}', 'creditcard': '\\textsc{Credit-card}', 'huffpost-topic': '\\textsc{HuffPost}-topic', 'huffpost-taxonomy': '\\textsc{HuffPost}-taxonomy', 'fmow': '\\textsc{fMoW}', 'cifar100': '\\textsc{CIFAR}-100'}
MODEL_TEX = {'gbt': 'Gradient-boosted trees', 'mlp': 'MLP head', 'linear': 'Linear probe', 'uncal': 'Linear probe (uncal.)', 'llm-icl': 'Frozen LLM classifier'}
CITE = {'ATC': '~\\cite{garg2022atc}', 'DoC': '~\\cite{guillory2021doc}', 'MANO': '~\\cite{xie2024mano}', 'PAPE/CBPE': '~\\cite{nannyml2024pape}', 'Prequential-delay': '~\\cite{grzenda2020delayed}', 'ADWIN-reset': '~\\cite{bifet2007adwin}', 'Naive seq. PPI': '~\\cite{bayesppi2025,csillag2025ppev}', 'MLDemon': '~\\cite{ginart2022mldemon}', 'IUPM-UI': '~\\cite{iupm2025}'}
ORDER = ['ATC', 'DoC', 'MANO', 'PAPE/CBPE', 'ADWIN-reset', 'Prequential-delay', 'Prequential-delay (best win.)', 'Naive seq. PPI', 'Discounted-label EB', 'Discounted-label EB (best win.)', 'StreamGauge', 'Oracle', 'Oracle (best win.)']
METHOD_TEX = {'MANO': 'Normalized score', 'PAPE/CBPE': 'Calibrated confidence', 'DoC': 'DoC-style'}
GROUP_BEFORE = {'ATC': '\\multicolumn{8}{@{}l}{\\emph{Label-free estimators (no interval)}} \\\\', 'ADWIN-reset': '\\midrule\n\\multicolumn{8}{@{}l}{\\emph{Delayed and sequential}} \\\\'}


def boot_ci(x, cluster=None, n=2000, seed=0):
    """Mean and half the bootstrap 2.5--97.5 percentile spread."""
    raise NotImplementedError('released upon publication')


def cell(m, h=0.0, nd=3, bold=False, under=False):
    raise NotImplementedError('released upon publication')


def write(name: str, body: str) -> None:
    raise NotImplementedError('released upon publication')


def read(block: str):
    raise NotImplementedError('released upon publication')


def counts(df) -> tuple[int, int]:
    raise NotImplementedError('released upon publication')


def main_comparisons(df: pd.DataFrame) -> pd.DataFrame:
    """Paired stream-level error tests with one Holm family of four rivals."""
    raise NotImplementedError('released upon publication')


def tab_datasets() -> None:
    raise NotImplementedError('released upon publication')


def tab_main() -> None:
    raise NotImplementedError('released upon publication')


REQ = {'- fixed-time EB wager': '\\req{2}', 'StreamGauge (full)': '---', '- staleness correction': '\\req{2}', '- transport charge': '\\req{3}', '- forgetting window': '\\req{1}', '- adaptive forgetting': '\\req{1}', '- inverse-propensity weighting': '\\req{2}', '- variance-adaptive radius': '\\req{2}', '- label-only fallback': '\\req{3}', '- decoupled centre': '\\req{4}', '- centre lag term': '\\req{4}', '- anchor (signal layer only)': '\\req{3}'}
ABL_LABEL = {'- fixed-time EB wager': 'fixed-time EB wager', '- staleness correction': 'staleness correction', '- transport charge': 'transport charge', '- forgetting window': 'forgetting window', '- adaptive forgetting': 'adaptive forgetting', '- inverse-propensity weighting': 'purchase IPW', '- variance-adaptive radius': 'variance-adaptive radius', '- label-only fallback': 'label-only fallback', '- decoupled centre': 'decoupled centre', '- centre lag term': 'centre lag term', '- anchor (signal layer only)': 'anchor (signal only)'}


def tab_ablation() -> None:
    raise NotImplementedError('released upon publication')


def tab_robustness() -> None:
    raise NotImplementedError('released upon publication')


def tab_generality() -> None:
    """RQ8: predictor family x modality."""
    raise NotImplementedError('released upon publication')


def tab_triage() -> None:
    """Both arms, each with its own modulus."""
    raise NotImplementedError('released upon publication')


def tab_instant() -> None:
    raise NotImplementedError('released upon publication')


def tab_cases() -> None:
    """Six timestamps off the drift episode, read by three monitors."""
    raise NotImplementedError('released upon publication')


def tab_efficiency() -> None:
    raise NotImplementedError('released upon publication')


def tab_certified() -> None:
    """The only block that tests the theorem instead of a surrogate."""
    raise NotImplementedError('released upon publication')


def tab_hparams() -> None:
    raise NotImplementedError('released upon publication')


def tab_regime() -> None:
    """Why a hindsight-tuned fixed window is not the same answer."""
    raise NotImplementedError('released upon publication')


def tab_score_sens() -> None:
    """How much of the comparison is the scorer's own smoothing bandwidth."""
    raise NotImplementedError('released upon publication')


def tab_rho() -> None:
    """The rate estimator, each mode read at its own calibrated multiplier."""
    raise NotImplementedError('released upon publication')


def tab_stationary() -> None:
    """What the drift insurance costs on a stream that does not drift."""
    raise NotImplementedError('released upon publication')


def tab_sharp() -> None:
    """Archived transport/tracking primitive checks, not a full identified set."""
    raise NotImplementedError('released upon publication')


def tab_certfrontier() -> None:
    """Archived partial proxies, kept separate from the certified theorem."""
    raise NotImplementedError('released upon publication')


def tab_serial() -> None:
    """What violating the independence hypothesis actually costs."""
    raise NotImplementedError('released upon publication')


def tab_horizon() -> None:
    """prop:degenerate: the saturation ladder and the look schedule."""
    raise NotImplementedError('released upon publication')


def tab_update() -> None:
    """What a mid-stream predictor change costs, and what a restart recovers."""
    raise NotImplementedError('released upon publication')


def tab_lrv() -> None:
    """Whether a long-run-variance layer repairs the independence violation."""
    raise NotImplementedError('released upon publication')


def tab_joint() -> None:
    """Purchase IPW and a stationary geometric maturity approximation."""
    raise NotImplementedError('released upon publication')


TABLES = {'datasets': tab_datasets, 'sharp': tab_sharp, 'serial': tab_serial, 'certfrontier': tab_certfrontier, 'hparams': tab_hparams, 'main': tab_main, 'regime': tab_regime, 'score_sens': tab_score_sens, 'rho': tab_rho, 'stationary': tab_stationary, 'ablation': tab_ablation, 'robustness': tab_robustness, 'generality': tab_generality, 'triage': tab_triage, 'instant': tab_instant, 'cases': tab_cases, 'efficiency': tab_efficiency, 'certified': tab_certified, 'horizon': tab_horizon, 'update': tab_update, 'lrv': tab_lrv, 'joint': tab_joint}


if __name__ == '__main__':
    raise NotImplementedError('released upon publication')
