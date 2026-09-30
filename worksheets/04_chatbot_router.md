# Worksheet 4: Corrective retrieval router · mental health chatbot `src/router.py`

Look at: `RouteDecision`, `classify_and_extract`, `route_question`, `route_with_correction`,
`route_all`, `_submit`, and `grade_relevance` in `src/grading.py`.

## Questions
1. What are the three paths `RouteDecision` can choose? Give one example question for each.
2. What is the `entity` field for? What entity should "what does 'I always fail' reflect?" produce?
3. `route_question` starts the vector search before the classifier finishes. Why? What does it cost if the path turns out to be `graph_rag`?
4. If the classifier call fails, what path is used?
5. In `route_with_correction`, what are the three grades, and what happens after each?
6. When is the web search fallback used, and when is it turned off? Why is it off during evals?
7. What does the `no_answer` path make the final answer do? Why is that better than answering from weak context?
8. `route_all` runs several sub questions. Where do sub questions come from?
9. What does `_submit` do with `contextvars`, and what breaks in LangSmith without it?
10. How many LLM calls can one user question cause in the worst case? Count them.

## Draw it
The full flow for "What is CBT and what disorders is it used for?"

## Interview answer
"What is corrective RAG, and how did you implement it?"

## Compare with C6 of the lab
Your chatbot never used BM25. Pick one question type where hybrid search would have helped it.
