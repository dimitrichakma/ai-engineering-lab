# Track 4: UI for AI apps (Streamlit)

Users judge an AI app by how it FEELS: does text stream, can I stop it, can I see what the agent
did, can I trust the answer? These three projects teach that, all in Streamlit.

| Project | Skill | Core? |
| --- | --- | --- |
| U1 streaming chat | streaming tokens, session state, stop and retry, history trimming | ⭐ |
| U2 agent UX | showing tool steps, citations, approve/reject before an action | ⭐ |
| U3 eval dashboard + theming | charts from eval results, a theme and a little CSS | |

## Rules for every UI project
- Keep logic OUT of the Streamlit file. `app.py` only draws; the logic sits in a plain Python
  module that pytest can test without a browser.
- Streamlit reruns the whole script on every click. Anything that must survive a rerun lives in
  `st.session_state`.
- Run: `uv run streamlit run track4_ui/u1_streaming_chat/app.py`
