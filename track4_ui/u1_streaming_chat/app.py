"""U1 Streamlit app. Run: uv run streamlit run track4_ui/u1_streaming_chat/app.py"""
import os

import streamlit as st

from track4_ui.u1_streaming_chat.chat_logic import (  # noqa: F401
    add_message, collect_stream, fake_stream, new_state, retry_last, trim_history,
)

st.set_page_config(page_title="U1 Streaming chat", page_icon="💬")

if "chat" not in st.session_state:
    st.session_state.chat = new_state()

# TODO 1: sidebar: model name (default from OLLAMA_MODEL), temperature slider, "Clear chat" button
# TODO 2: draw every message in st.session_state.chat["messages"] with st.chat_message(role)
# TODO 3: on st.chat_input: add the user message, then stream the reply inside
#         st.chat_message("assistant") with st.write_stream(...)
#         Use ollama.chat(model, messages=trim_history(...), stream=True) and yield chunk.message.content,
#         or fake_stream() when LLM_PROVIDER=fake
# TODO 4: Stop button sets st.session_state.stop = True; your generator checks it (see collect_stream)
# TODO 5: Retry button: text = retry_last(state); if text, stream a new answer for it
_ = os
