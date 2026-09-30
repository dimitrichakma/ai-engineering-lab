# M1: Model selection

**Time:** 1 evening (plus download time) · **Skill:** choosing a model with numbers, not vibes.

## Setup
Pull three small models that fit your laptop, for example:
`ollama pull qwen2.5:3b`, `ollama pull llama3.2:3b`, `ollama pull gemma3:4b`
(check `ollama list` and free disk space first; each is about 2 to 3 GB).

## The eval set
Reuse the S3 ticket triage data: `track1_structured_output/s3_ticket_triage/data/tickets.csv`
(20 tickets with a category). Same prompt, same schema, temperature 0, for every model.

## What you write in `compare.py`
1. `run_model(model, rows) -> list[Result]`: for each ticket, call Ollama with structured output,
   record `pred`, `valid_json` (did it parse?), `latency_ms`, and `eval_count` / `prompt_eval_count`
   from the Ollama response (token counts).
2. `score(results) -> dict` (tested): accuracy, valid_json_rate, p50 and p95 latency,
   tokens per second (output tokens / generation seconds).
3. Memory: after a run, `ollama ps` shows the model size in memory. Record it by hand.
4. `pick(scores, max_p95_ms)`: best accuracy among models under the latency limit; ties go to the faster one.
5. Save all results to `results/m1.csv` in the U3 dashboard format and look at them there.

## Done when
- [ ] `uv run pytest track6_models/m1_model_selection` passes.
- [ ] A table: model, accuracy, valid JSON %, p95 latency, tokens/s, memory. Plus your choice and one
      paragraph why. Run twice: are the numbers stable? (20 examples is small; say so.)
