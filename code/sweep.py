# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "scipy", "pandas", "scikit-learn", "pyarrow"]
# ///
"""Evaluate SGConfig variants side by side on the cached streams."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import argparse
import json
import os
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import pandas as pd
from run_experiments import BUDGET, BURN, DEFAULT_DELAY, available, draw_delay, load
from streamgauge import SGConfig, run_streamgauge, score
from streams import SPECS


WORKERS = int(os.environ.get('SG_WORKERS', max(1, (os.cpu_count() or 4) - 2)))
ORDER = ['insects-abrupt', 'huffpost-taxonomy', 'creditcard', 'electricity', 'insects-gradual', 'covertype', 'airlines', 'huffpost-topic', 'cifar100', 'fmow']
METRICS = ['error', 'coverage', 'width', 'abstain', 'used_lab', 'ever_missed', 'max_miss_run', 'coverage_reported', 'report_rate']


def run(variants: list[tuple[str, dict]], streams: list[str], seeds: list[int]):
    raise NotImplementedError('released upon publication')


def report(df: pd.DataFrame, base: str='default') -> pd.DataFrame:
    """Aggregate, plus the two quantities a candidate has to win on."""
    raise NotImplementedError('released upon publication')


def main() -> int:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    raise SystemExit(main())
