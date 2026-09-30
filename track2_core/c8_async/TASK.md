# C8: Async batching

**Time:** 1 to 2 evenings · **Fills a gap:** your chatbot runs work in parallel with threads
(`ThreadPoolExecutor` in `router.py`); here you learn the `asyncio` way and measure it.

## The idea
You have 100 texts to classify. One by one, at 1 second each, that's 100 seconds. Sending all 100
at once can overload the model server or hit rate limits. The right way: run them **concurrently
with a limit**, for example at most 8 at a time, using `asyncio.Semaphore`.

## What is given
`fake_llm.py`: `FakeAsyncLLM(delay, fail_every)`, an async fake model that sleeps and
sometimes fails. It records the **highest number of calls running at the same time**, so tests can
check your limit works.

## What you write in `batch.py`
1. `run_sequential(items, llm)`: one after another (the baseline).
2. `run_concurrent(items, llm, limit)`: `asyncio.gather` + `asyncio.Semaphore(limit)`.
   - Results must come back in the **same order** as the input.
   - One failed item must not crash the batch: return a `Result(ok=False, error=...)` for it.
3. `benchmark()`: time sequential vs limit 2, 4, 8, 16 with the fake model and print a table.
4. Real run (optional): `ollama.AsyncClient().chat(...)` on 20 texts from the C2 guardrails CSV.
   Does the speedup match the fake? (A local model on a laptop may not speed up much. Why?)

## Done when
- [ ] With the fake model (0.1 s delay), 40 items at limit 8 finish in about 0.5 s, not 4 s.
- [ ] The fake model never sees more than `limit` calls at once (tested).
- [ ] A failing item gives `ok=False` and all other items still succeed (tested).
- [ ] Output order matches input order (tested).

## Questions for your log
- Threads vs asyncio: when is each the better choice?
- What limit would you pick for a paid API with a rate limit of 50 requests per minute?
