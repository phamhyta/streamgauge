# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pandas", "pyarrow", "requests", "scikit-learn"]
# ///
"""A frozen LLM classifier as the monitored predictor, served via OpenRouter."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import json
import os
import pathlib
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import requests


ENDPOINT = 'https://openrouter.ai/api/v1/chat/completions'
MODEL = os.environ.get('SG_LLM_MODEL', 'qwen/qwen3-30b-a3b-instruct-2507')
N_SHOT = 16
MAX_WORKERS = 24
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TOP_LOGPROBS = int(os.environ.get('SG_LLM_TOP_LOGPROBS', '20'))


def build_llm_stream(name: str, seed: int=0) -> dict:
    raise NotImplementedError('released upon publication')


def dry_run(name='huffpost-taxonomy'):
    """Show the frozen prompt and estimate spend. Makes no API call."""
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    raise NotImplementedError('released upon publication')
