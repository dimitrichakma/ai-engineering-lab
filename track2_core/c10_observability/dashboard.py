"""Run: uv run streamlit run track2_core/c10_observability/dashboard.py"""
import json
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Trace dashboard", layout="wide")
st.title("Trace dashboard")

path = Path("traces.jsonl")
if not path.exists():
    st.info("No traces yet. Run: uv run python -m track2_core.c10_observability.pipeline")
    st.stop()

records = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

# TODO 1: top row of st.metric: requests, error rate, p50 and p95 request latency, total cost
# TODO 2: bar chart of average duration per step name (guard / retrieve / generate)
# TODO 3: table of the 10 slowest "request" spans
# TODO 4: st.selectbox to pick one trace_id; show its spans as a waterfall
#         (hint: a horizontal bar per span, x = start offset to end, e.g. with st.bar_chart or altair)
st.write(f"{len(records)} spans loaded")
