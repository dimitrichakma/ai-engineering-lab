# C10: Observability (tracing by hand + a dashboard)

**Time:** 1 to 2 evenings · **Rebuilds:** the idea behind LangSmith tracing and the correlation id
in your habit tracker. **New skill:** you build the tracing yourself and read it in a dashboard.

## The idea
When a user says "it was slow" or "it gave a wrong answer", you need to see **every step** of that
one request: what ran, how long it took, how many tokens it used, what it cost, and where it failed.
A **trace** is one request. A **span** is one step inside it. Spans can have a parent span.

## What you write
1. `tracing.py`
   - a `trace_id` stored in a `contextvars.ContextVar`, set once per request with `new_trace()`
   - `span(name, **attrs)`: a context manager that records start time, duration in ms, status
     (`ok` / `error`), error message, parent span id, and any attrs you add inside with
     `current_span().set(tokens_in=..., tokens_out=..., cost_usd=...)`
   - every finished span is appended as one JSON line to `traces.jsonl`
2. `pipeline.py` (given skeleton): a fake 3 step request `guard → retrieve → generate` with random
   delays and a 10% error rate. Wrap each step and the whole request in spans. Run 50 requests.
3. `dashboard.py` (Streamlit): read `traces.jsonl` and show
   - requests, error rate, p50 and p95 latency, total cost
   - average duration per step (bar chart): which step is slowest?
   - a table of the 10 slowest requests; pick one to see its spans as a waterfall

## Done when
- [ ] Nested spans get the right parent id (tested).
- [ ] A span that raises is recorded with `status="error"` and the error still propagates (tested).
- [ ] `uv run streamlit run track2_core/c10_observability/dashboard.py` shows all the parts above.

## Questions for your log
- What should you NEVER write into a trace? (Think about Somajji and personal data.)
- p95 vs average latency: why do teams care more about p95?
