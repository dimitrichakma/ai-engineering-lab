"""Eval metrics for the dashboard (no Streamlit here)."""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data" / "results.csv"


def load_results(path: Path = DATA) -> pd.DataFrame:
    # TODO
    raise NotImplementedError


def summary(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: groupby run_id -> model, accuracy (pred == gold mean), p50_latency_ms, p95_latency_ms
    #       (quantile 0.5 / 0.95), avg_tokens. Sort by accuracy descending. Index = run_id.
    raise NotImplementedError


def confusion(df: pd.DataFrame, run_id: str) -> pd.DataFrame:
    # TODO: pd.crosstab(gold, pred) for that run, with all labels on both axes, 0 where empty
    raise NotImplementedError


def worst_examples(df: pd.DataFrame, run_id: str, n: int = 10) -> pd.DataFrame:
    # TODO: wrong rows for the run, sorted by latency_ms descending, first n
    raise NotImplementedError
