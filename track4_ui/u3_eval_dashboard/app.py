"""U3 dashboard. Run: uv run streamlit run track4_ui/u3_eval_dashboard/app.py"""
from pathlib import Path

import streamlit as st

from track4_ui.u3_eval_dashboard.metrics import (  # noqa: F401
    confusion, load_results, summary, worst_examples,
)

st.set_page_config(page_title="Eval dashboard", page_icon="📊", layout="wide")

css = (Path(__file__).parent / "style.css").read_text()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# TODO 1: df = load_results(); s = summary(df)
# TODO 2: three st.metric cards in st.columns(3) for the best run (delta vs the second best)
# TODO 3: st.bar_chart of accuracy per run + st.dataframe(s)
# TODO 4: run picker (st.selectbox) -> confusion matrix + worst_examples table
# TODO 5: cache load_results with @st.cache_data so it doesn't reload on every click
