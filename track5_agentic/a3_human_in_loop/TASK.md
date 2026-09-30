# A3: Human in the loop + durable runs (LangGraph) ⭐

**Time:** 2 evenings · **Skill:** an agent that stops, waits for a person (minutes or days), and
continues exactly where it stopped, even after the program restarts.

This is the only LangGraph project in the lab. You already built loops by hand, so here you learn
what a framework adds: **checkpoints** (state saved after every step) and **interrupts** (pause
and resume).

## The flow: a refund agent
`classify` → `draft_reply` → **`human_review` (interrupt)** → `send_reply` or `revise`
- `classify`: reads the customer message, sets `refund_amount`.
- `draft_reply`: writes a reply.
- `human_review`: calls `interrupt({...})` with the draft and amount. The graph stops here.
  A person resumes with `Command(resume={"approved": True})` or
  `Command(resume={"approved": False, "note": "be kinder"})`.
- Rejected → `draft_reply` again with the note. Approved → `send_reply` (a fake sender that
  records what was sent). Amounts above `AUTO_LIMIT` must never skip review.

## What you write in `graph.py`
1. The `State` TypedDict (given) and the four node functions.
2. `build_graph(checkpointer, llm)`: nodes, edges, and a conditional edge after review.
3. A small CLI `run.py` that lists paused runs and lets you approve or reject by thread id,
   using `SqliteSaver` so a paused run survives closing the terminal.

Read the CURRENT docs before starting (the API moves fast):
https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
https://langchain-ai.github.io/langgraph/concepts/persistence/

## Done when
- [ ] `uv run pytest track5_agentic/a3_human_in_loop` passes (uses the in memory checkpointer).
- [ ] With `run.py`: start a run, close the terminal, open it again, approve, and the reply is sent.
- [ ] Log: what did LangGraph save you, and what did it hide from you, compared with A1?
