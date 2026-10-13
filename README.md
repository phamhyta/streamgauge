# StreamGauge — Certifying a Moving Target

Public code repository for the paper **_Certifying a Moving Target: Streaming Model Evaluation
under Concept Drift and Lagged Labels_** (under review). `StreamGauge` is the evaluation layer the
paper develops: an online monitor of a deployed model's current accuracy when the verifying labels
arrive late.

> **Status: skeleton release.** This repository currently contains the module structure, API
> signatures, and documentation of the full pipeline. The complete implementation, cached
> streams, and replay seeds will be released here under an open-source license upon publication.

## What StreamGauge does

A model serving a changing data stream must be watched for silent degradation, but its labels
arrive **late**, so any evaluation built from them describes the model as it was, not as it is.
Label-free scores are immediate but unanchored; delayed labels are anchored but stale.
**StreamGauge** combines serving-time correctness scores with a sparse, budgeted stream of delayed
labels that rectify them, charges for the age gap between the evidence and the present through an
optimal-transport correction under a declared drift envelope, and reports an interval that remains
valid under repeated inspection. When that interval is wider than a useful-width target, the
monitor **abstains** and names the binding term.

Two modes are provided:

- **Operational** (`streamgauge.py`) — estimates drift and uses aggregate empirical-Bernstein radii;
  constant time per item.
- **Certified** (`certified_streamgauge.py`) — an auditable reference implementation of the
  certified transport confidence tube over predeclared window grids and look schedules.

## Repository layout

```
code/      Python: data download, stream construction, monitors, baselines, experiments, figures
data/      Downloaded public streams and frozen-predictor caches (not committed)
results/   One parquet per experiment block (published upon full release)
```

### Pipeline modules (`code/`)

| Module | Role |
| --- | --- |
| `fetch_data.py` | Download the public streams (OpenML, USP Insects, HuffPost, FMoW, CIFAR-100) |
| `streams.py` | Train a predictor once on a warm-up prefix, freeze it, and emit (correctness, signal, confidence) per item |
| `llm_stream.py` | Frozen LLM in-context classifier as the monitored predictor |
| `streamgauge.py` | StreamGauge (operational mode), passive baselines, scoring utilities |
| `certified_streamgauge.py` | Certified transport confidence tube and the scheduled variance-adaptive refinement |
| `baselines_query.py` | Active-querying monitors for the zero-latency limit |
| `run_experiments.py` | Every experiment block; writes `results/<block>.parquet` |
| `sweep.py` | Side-by-side evaluation of `SGConfig` variants |
| `sharpness_lp.py` | Numerical check that the identified half-width is attained |
| `cert_frontier.py` | Best attainable certified width under alternative radii |
| `make_tables.py`, `gen_figs.py` | Render every table and figure from `results/` |

## Reproducing (upon full release)

All experiments are CPU-scale (cached frozen-predictor streams; replays under many delay/budget
draws). Each script declares its own dependencies (PEP 723), so `uv run` works without a separate
environment:

```bash
uv run code/fetch_data.py          # download the public streams into data/
uv run code/streams.py             # build the frozen-predictor stream caches
uv run code/streamgauge.py         # self-check of the operational monitor
uv run code/run_experiments.py     # all experiment blocks (or: run_experiments.py rq1 rq4)
uv run code/make_tables.py         # LaTeX tables
uv run code/gen_figs.py            # figures
```

Alternatively, `pip install -r requirements.txt` and run the scripts with `python`.

## Data

Every stream used in the paper is public and downloaded directly from its source by
`code/fetch_data.py`: Electricity, Airlines, Covertype and Credit-card fraud (OpenML), USP Insects
(abrupt and gradual), the HuffPost News Category dataset, FMoW, and CIFAR-100. No data is
redistributed in this repository.

## Citation

Citation information will be added upon publication.

## License

[MIT](LICENSE)
