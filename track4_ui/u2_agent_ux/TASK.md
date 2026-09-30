# U2: Agent UX ⭐

**Time:** 1 to 2 evenings · **Skill:** making an agent's work VISIBLE and SAFE to the user.

People trust an agent when they can see what it did, where an answer came from, and when it
asks before doing something risky. This project builds those three pieces.

## The agent (given, fake)
`agent_steps.py` has `run_fake_agent(question)` that yields events like:
`{"type": "tool_call", "tool": "search_docs", "args": {...}}`,
`{"type": "tool_result", "tool": "search_docs", "result": [...]}`,
`{"type": "needs_approval", "action": "send_email", "args": {...}}`,
`{"type": "answer", "text": "... [1] ... [2]", "sources": [...]}`.
Later you can swap in your C1 or A1 agent: it only has to yield the same events.

## What you write
### `agent_steps.py` (tested)
1. `summarize_step(event) -> str`: one short human line per event, for example
   `"🔎 Searching docs for: refund policy"`. Unknown types → `"Working..."`.
2. `render_citations(text, sources) -> tuple[str, list[str]]`: keeps `[n]` markers that point to a
   real source, removes markers with no source, and returns the footnote list
   `["[1] Refund policy (page 2)", ...]` in order of first use.
3. `ApprovalGate`: `request(action, args) -> id`, `decide(id, approved: bool)`, `status(id)`
   returning `pending | approved | rejected`. Deciding twice raises `ValueError`.
   Risky actions (`RISKY = {"send_email", "delete_record", "make_payment"}`) always need approval.

### `app.py` (Streamlit)
- Tool steps inside `st.status("Agent is working...", expanded=False)`, one line per step.
- The answer with footnotes; each source in an `st.expander`.
- On `needs_approval`: show the action and args with **Approve** and **Reject** buttons. The agent
  only continues after a decision. Keep the gate in `st.session_state`.

## Done when
- [ ] `uv run pytest track4_ui/u2_agent_ux` passes.
- [ ] A user can see every tool the agent used, and nothing risky happens without a click.
