# C6: Retrieval experiments

**Time:** 1 to 2 evenings · **Rebuilds:** chatbot `src/retrieval.py`, habit tracker `src/vector_store.py`

## The idea
Most RAG apps fail because **retrieval** is weak, not the LLM. Here you don't guess, you measure.
You compare chunking strategies and search methods on a fixed question set and pick the winner
with numbers.

## The setup
- `data/handbook.md`: a fictional 10 section employee handbook.
- `data/questions.json`: 20 questions. Each has `answer_contains`, a phrase that must appear in a
  retrieved chunk for it to count as a **hit**. (This works for any chunking, unlike chunk ids.)
- Embeddings: `ollama.embed(model="nomic-embed-text", input=[...])` → `.embeddings` (a list of vectors).
- Keyword search: `rank_bm25.BM25Okapi`.

## What you write
1. `chunkers.py`
   - `fixed_size(text, size_words, overlap_words)`
   - `by_heading(text)`: one chunk per `##` section
2. `search.py`
   - `VectorIndex(chunks)`: embed once, `search(query, k)` by cosine similarity (write cosine yourself with plain Python or numpy)
   - `BM25Index(chunks)`: `search(query, k)`
   - `hybrid_search(query, k, vec, bm25)`: combine with **Reciprocal Rank Fusion**:
     `score(chunk) = sum over lists of 1 / (60 + rank)`
3. `experiment.py`: for each setup, compute **hit@1, hit@3, hit@5** and print one table:

| Setup | hit@1 | hit@3 | hit@5 |
| --- | --- | --- | --- |
| fixed 40 words, overlap 10, vector | | | |
| fixed 120 words, overlap 20, vector | | | |
| by heading, vector | | | |
| by heading, BM25 | | | |
| by heading, hybrid | | | |

## Done when
- [ ] The table prints with real numbers for all 5 setups.
- [ ] Chunkers and RRF are unit tested (no model calls).
- [ ] You list, in the log, 2 questions that fail everywhere and explain why.

## Questions for your log
- Which setup won? Is it the one you expected?
- Question 9 says "Uber" but the handbook says "ride sharing". Which method handles that better, and why?
- Your chatbot used vector search + a graph. Where would BM25 have helped it?
