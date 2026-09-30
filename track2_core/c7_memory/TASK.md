# C7: Memory and history trimming

**Time:** 1 to 2 evenings · **Rebuilds:** habit tracker `_trim_history` / `trim_history` in
`src/agent.py` and `src/summarize_memory.py`

## The idea
Model APIs are stateless: every turn re-sends the whole conversation. Your habit tracker's README
says an old thread once used up the daily token budget "in three messages". The fix was
`trim_messages(strategy="last", max_tokens=6000, start_on="human")`. Here you write that yourself,
then add **summary memory**: old turns become one short summary instead of disappearing.

## Rules your trimmer must follow (same as your habit tracker)
1. Keep the system message always (it's counted separately).
2. Keep the **most recent** messages that fit in `max_tokens`.
3. The kept history must **start on a user message**, never on an assistant reply or a tool
   result. (Why? The API rejects a tool result without its tool call.)
4. Never cut a message in half.

## What you write in `memory.py`
1. `count_tokens(text)`: approximate, `len(text) / 4` rounded up. (Stretch: compare with the real
   count Ollama returns in `prompt_eval_count`.)
2. `trim_history(messages, max_tokens) -> list`: the 4 rules above.
3. `SummaryMemory(max_recent_tokens, summarize_fn)`:
   - `add(message)`
   - `context() -> list`: `[system, {"role": "system", "content": "Summary of earlier: ..."}, *recent]`
   - when recent messages exceed the budget, the oldest ones are folded into the running summary
     with `summarize_fn(old_summary, messages_to_fold) -> str`.
4. `chat.py`: a small command line chat using `SummaryMemory` and `generate_text`. Print the token
   count sent each turn.

## Done when
- [ ] `trim_history` tests pass, including "never starts on a tool or assistant message".
- [ ] `SummaryMemory` tests pass with a fake summarizer (no LLM).
- [ ] In `chat.py`, after 20 turns the tokens sent per turn stay under your budget.

## Questions for your log
- What does the model forget with plain trimming that it keeps with summary memory? What can the
  summary get wrong?
- Your habit tracker also stores weekly summaries in pgvector. How is that different from this?
