# C2: Guardrail pipeline (and measuring it)

**Time:** 1 to 2 evenings · **Rebuilds:** habit tracker `input_guardrail` / `output_guardrail` in `src/agent.py`

## The idea
Your habit tracker screens every message in layers:
1. a **regex pre filter** for obvious attacks (fast, free),
2. an **LLM classifier** with a structured verdict (category + confidence),
3. a **confidence threshold** for off topic (below it, let the coach redirect instead of blocking),
4. **fail safe**: if the classifier errors or times out, block.

Here you rebuild that for a **study planner coach**, and then do something your habit tracker
tests don't: **measure** it on a labeled set, including how often it wrongly blocks normal messages.

## Why false positives matter
A guardrail that blocks every attack but also blocks 1 in 5 normal messages is a broken product.
Your habit tracker learned this: "the lesson isn't done yet" was once wrongly treated as off topic.

## What you write
1. `guard.py`
   - `Verdict` (Pydantic): `category` in `safe | injection | harmful | off_topic`, `confidence` 0 to 1, `reason`
   - `INJECTION_PATTERNS`: at least 4 regexes
   - `classify(text, llm=generate_json) -> Verdict`
   - `check_input(text, llm=generate_json) -> Decision` with `allowed: bool`, `category`, `source`
     (`"regex" | "llm" | "fail_safe" | "threshold"`)
2. `evaluate.py`: run all of `data/messages.csv` and print:
   - **attack block rate** (injection + harmful blocked / total injection + harmful)
   - **false positive rate** (safe messages blocked / total safe)
   - which layer blocked each one (regex vs LLM)
   - the list of mistakes
3. Try 2 versions: threshold 0.6 vs 0.85. Log both results.

## Done when
- [ ] Classifier error or timeout → blocked with `source="fail_safe"` (tested with a fake llm).
- [ ] Off topic below the threshold → allowed with `source="threshold"` (tested).
- [ ] `evaluate.py` prints both rates. Numbers logged for 2 thresholds.
- [ ] All tests pass.

## Stretch
- Add an output check: regex for leaked internals (your tool names, "system prompt"), like `_LEAK_PATTERNS`.
- Write 10 NEW attacks yourself that get past your guard. Then fix the guard.
