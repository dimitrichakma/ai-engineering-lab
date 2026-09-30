# C9: Caching (exact + semantic)

**Time:** 1 to 2 evenings · **Rebuilds:** chatbot `src/llm_cache.py` (exact match, Postgres).
**New skill:** semantic caching, and measuring when it gives a WRONG answer.

## The idea
- **Exact cache:** same model + same prompt + same settings → return the saved answer. Safe, but
  "How do I get a refund?" and "how can I get my refund" are two misses.
- **Semantic cache:** embed the question; if a saved question is similar enough (cosine ≥ threshold),
  reuse its answer. More hits, but a real risk: "refund for a **bus** ticket" vs "refund for a
  **train** ticket" are very similar sentences with different answers.

## What you write in `cache.py`
1. `cache_key(model, prompt, settings) -> str`: a SHA256 of a stable JSON string (sorted keys).
2. `ExactCache(path)`: SQLite table `(key PRIMARY KEY, answer, created_at)`, `get(key)`, `set(key, answer)`,
   plus a TTL: entries older than `ttl_seconds` count as a miss.
3. `SemanticCache(embed_fn, threshold)`: in memory list of (vector, question, answer);
   `get(question) -> (answer, score) | None`, `set(question, answer)`.
4. `cached_generate(prompt, llm, exact, semantic)`: exact first, then semantic, then the model;
   save the result to both. Return `(answer, source)` where source is `exact | semantic | model`.

## Measure it (`experiment.py`)
`data/pairs.csv` has question pairs labelled `same` (a hit is correct) or `different` (a hit is WRONG).
For thresholds 0.80, 0.85, 0.90, 0.95 print: **correct hits**, **wrong hits**, **misses**.
Pick a threshold and explain the trade off in your log.

## Done when
- [ ] Exact cache tests pass, including TTL expiry with a fake clock.
- [ ] Semantic cache tests pass with a fake embed function (no model).
- [ ] The threshold table prints with real embeddings (`nomic-embed-text`).

## Questions for your log
- Would you use a semantic cache for Somajji? For which part, if any? (Think about wrong hits.)
- Why must the cache key include the model name and settings?
