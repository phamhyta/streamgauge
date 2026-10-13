# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pandas", "scipy", "pyarrow", "requests"]
# ///
"""Fetch the real streams used in the StreamGauge evaluation."""
# NOTE: skeleton stub -- the full implementation, cached streams, and replay
# seeds will be released upon publication.

from __future__ import annotations
import io
import json
import pathlib
import sys
import zipfile
import numpy as np
import pandas as pd
import requests


DATA = pathlib.Path(__file__).resolve().parent.parent / 'data'
OPENML = {'electricity': 151, 'airlines': 1169, 'covertype': 1596, 'creditcard': 1597}
INSECTS = {'insects_abrupt': '1WQoIuuVgiuXfzv4kvao6XuLQG37V923O', 'insects_gradual': '1_WJ7lxK2sx1i6kq9Nqv4KrjT0ZXB0QbC'}
HUFFPOST = 'https://huggingface.co/api/datasets/heegyu/news-category-dataset/parquet/default/train/0.parquet'
FMOW = 'https://huggingface.co/datasets/jbourcier/fmow-rgb-baseline/resolve/main/'
FMOW_PARTS = ['val-metadata.tar.gz', 'val-images.tar.gz']
CIFAR100 = 'https://huggingface.co/api/datasets/uoft-cs/cifar100/parquet/cifar100/train/0.parquet'


def fetch_openml(name: str, did: int) -> None:
    raise NotImplementedError('released upon publication')


def fetch_insects(name: str, gdrive_id: str) -> None:
    raise NotImplementedError('released upon publication')


def fetch_huffpost() -> None:
    raise NotImplementedError('released upon publication')


def fetch_fmow() -> None:
    """fMoW val split -> extracted JPEGs plus a timestamp-sorted index."""
    raise NotImplementedError('released upon publication')


def fetch_cifar100() -> None:
    raise NotImplementedError('released upon publication')


if __name__ == '__main__':
    raise NotImplementedError('released upon publication')
