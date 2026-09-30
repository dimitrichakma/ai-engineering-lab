# A6: Agent evaluation ⭐

**Time:** 1 to 2 evenings · **Skill:** measuring an agent, not just one answer. An agent can reach
the right answer by a wasteful or dangerous path, and that matters.

## What we measure per case
- **Success:** is the final answer correct? (exact match or a "must contain" check)
- **Trajectory:** did it call the tools it needed (**recall**), avoid tools it didn't need
  (**precision**), keep required order, and never call a **forbidden** tool?
- **Cost:** steps, model calls, tokens, and a cost in USD using a price table (local models are $0,
  but you compute what it WOULD cost on a paid API, which is how teams decide).
- **Latency.**

## Data
`data/cases.jsonl`: each case has `question`, `expected_answer_contains`, `required_tools`
(in order), `forbidden_tools`. `data/sample_traces.jsonl`: saved runs of a fake agent, so you
can build the scoring before running a real one.

## What you write in `agent_eval.py`
1. `score_case(case, trace) -> CaseScore` (see the fields in the file).
2. `in_order(required, called) -> bool`: required tools appear in this order (others may be between).
3. `cost_usd(trace, prices)`: sum of input and output tokens times the price per million tokens.
4. `summarize(scores) -> dict`: success rate, mean precision/recall, forbidden call count,
   mean steps, p95 latency, total cost.
5. `main`: score the sample traces and print a table. Then record traces from YOUR A1 or C1 agent
   (reuse C10 tracing) and score them too.

## Done when
- [ ] `uv run pytest track5_agentic/a6_agent_eval` passes.
- [ ] A table comparing two agent versions (for example A1 plan and execute vs C1 tool loop).
- [ ] Log: one case where the answer was right but the trajectory was bad. Why does it matter?
