# U1: Streaming chat ⭐

**Time:** 1 evening · **Rebuilds:** the chat screen of your mental health chatbot, properly.
**Skill:** a chat UI that streams tokens, remembers the conversation, and lets the user stop or retry.

## What you write
### `chat_logic.py` (pure Python, tested)
1. `new_state() -> dict` with `messages` (list of `{"role", "content"}`) and `stopped: False`.
2. `add_message(state, role, content)`; role must be `user` or `assistant` (else `ValueError`).
3. `trim_history(messages, max_messages)`: keep the system message (if any) plus the LAST
   `max_messages` others. Reuse your C7 idea.
4. `collect_stream(chunks, should_stop)`: joins text chunks until `should_stop()` returns True.
   Returns `(text, stopped)`. This is how "Stop" works without threads.
5. `retry_last(state)`: removes the last assistant message and returns the last user message,
   so the app can ask again. Returns `None` if there is nothing to retry.

### `app.py` (Streamlit, not tested)
- Show history with `st.chat_message`; input with `st.chat_input`.
- Stream with `st.write_stream` from `ollama.chat(..., stream=True)` (or the fake stream).
- A **Stop** button that sets a flag in `st.session_state`, and a **Retry** button.
- A sidebar with model name, temperature, and a "Clear chat" button.

## Done when
- [ ] `uv run pytest track4_ui/u1_streaming_chat` passes.
- [ ] Text appears word by word; Clear, Stop and Retry work.
- [ ] Refreshing the browser page loses the chat. Write in your log why, and how you'd keep it.
