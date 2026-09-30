# M2: Embedding model comparison

**Time:** 1 evening · **Skill:** picking an embedding model by measuring retrieval on your own data.

## Setup
`ollama pull nomic-embed-text`, `ollama pull mxbai-embed-large`, `ollama pull all-minilm`
(check sizes first). Optional: `bge-m3`, which is multilingual; try it on a few Bangla questions.

## Data
Reuse C6: `track2_core/c6_retrieval/data/handbook.md` and `questions.json`.
Chunk with your C6 `by_heading` chunker so only the embedding model changes.

## What you write in `compare_embeddings.py`
1. `embed_all(model, texts, batch=16)`: `ollama.embed(model=..., input=batch).embeddings`; time it.
2. `rank(query_vec, chunk_vecs) -> list[int]`: chunk indexes by cosine, best first.
3. Metrics (tested): `hit_at_k(ranked_hits, k)` and `mrr(ranked_hits)` where `ranked_hits` is a
   list of booleans per question ("is the chunk at this rank correct?").
   A chunk is correct if it contains the question's `answer_contains` text.
4. For each model print: hit@1, hit@3, MRR, dimensions, seconds to embed all chunks.

## Things to notice (write them in your log)
- Some models need a prefix, for example nomic uses `search_query: ` and `search_document: `.
  Measure with and without it.
- Bigger vectors cost more storage and search time. Is the quality gain worth it?
- You can never compare vectors from two different models. Changing the model means re-embedding everything.

## Done when
- [ ] `uv run pytest track6_models/m2_embeddings` passes.
- [ ] A table for 3 models (and the prefix experiment), plus your pick.
