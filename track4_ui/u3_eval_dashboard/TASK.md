# U3: Eval dashboard + theming

**Time:** 1 evening · **Skill:** turning eval results into a page a teammate can read in 30 seconds,
and giving Streamlit your own look with a theme and a little CSS.

## Data
`data/results.csv`: one row per (run, example): `run_id, model, example_id, gold, pred, latency_ms, tokens`.
Three runs of a 4 class ticket classifier (sample data). Later, point it at your own C4/M1 results.

## What you write
### `metrics.py` (tested)
1. `load_results(path) -> pd.DataFrame`
2. `summary(df) -> pd.DataFrame`: one row per `run_id` with `model, accuracy, p50_latency_ms,
   p95_latency_ms, avg_tokens`, sorted by accuracy (best first).
3. `confusion(df, run_id) -> pd.DataFrame`: gold as rows, pred as columns, counts (0 where empty).
4. `worst_examples(df, run_id, n)`: the wrong predictions, slowest first.

### `app.py` (Streamlit)
- `st.metric` cards for the best run (accuracy, p95 latency) with the difference to the second best.
- A bar chart of accuracy per run and a table from `summary`.
- A run picker → confusion matrix + wrong examples table.

### Theming
- `.streamlit/config.toml`: pick your colors (given as a start).
- `style.css`: a few rules only (card look for metrics, a font). Load it with
  `st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)`.
  Keep it small: heavy CSS breaks when Streamlit updates its HTML.

## Done when
- [ ] `uv run pytest track4_ui/u3_eval_dashboard` passes.
- [ ] Someone who has never seen the project can say which model is best, and why, in 30 seconds.
