# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pandas", "scikit-learn", "pyarrow",
#                 "sentence-transformers", "torch", "torchvision",
#                 "transformers", "pillow"]
# # torchvision is not optional: AutoImageProcessor refuses to load without it,
# # and the failure only surfaces on the image arms.
# ///
"""Turn each downloaded dataset into a monitored stream."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import io
import pathlib
import numpy as np
import pandas as pd


DATA = pathlib.Path(__file__).resolve().parent.parent / 'data'
CACHE = DATA / 'streams'
WARMUP = 10000
MAX_LEN = 60000
SPECS = {'insects-abrupt': ('insects_abrupt.parquet', 'class', 'abrupt'), 'insects-gradual': ('insects_gradual.parquet', 'class', 'gradual'), 'electricity': ('electricity.parquet', 'class', 'recurring'), 'airlines': ('airlines.parquet', 'Delay', 'mixed'), 'covertype': ('covertype.parquet', 'class', 'ordered/natural'), 'creditcard': ('creditcard.parquet', 'Class', 'injected concept')}
TAXONOMY_OLD = ['WELLNESS', 'PARENTING', 'STYLE & BEAUTY', 'ENVIRONMENT', 'CULTURE & ARTS', 'WORLDPOST']
TAXONOMY_NEW = ['HEALTHY LIVING', 'PARENTS', 'STYLE', 'GREEN', 'ARTS', 'ARTS & CULTURE', 'THE WORLDPOST', 'WORLD NEWS']
TEXT_SPECS = {'huffpost-taxonomy': (TAXONOMY_OLD + TAXONOMY_NEW, 'natural pure concept'), 'huffpost-topic': (None, 'natural mixed')}
TEXT_TOPK = 12
EMBED_MODEL = 'all-MiniLM-L6-v2'
IMAGE_SPECS = {'fmow': 'natural temporal', 'cifar100': 'injected concept'}
VISION_MODEL = 'facebook/dinov2-base'
IMAGE_TOPK = 20
ALL_SPECS = list(SPECS) + list(TEXT_SPECS) + list(IMAGE_SPECS)
MODELS = ('gbt', 'mlp', 'linear', 'uncal', 'llm-icl')


def model_applies(model: str, stream: str) -> bool:
    """`llm-icl` needs raw text; `gbt` is the tabular default, not a probe."""
    raise NotImplementedError('released upon publication')


REFIT_WIN = 10000


def build(name: str, seed: int=0, model: str='gbt', refit_at: int | None=None) -> dict:
    """One stream. With `refit_at`, the predictor is RETRAINED partway through."""
    raise NotImplementedError('released upon publication')


def report() -> None:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    raise NotImplementedError('released upon publication')
