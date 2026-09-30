"""U2 Streamlit app. Run: uv run streamlit run track4_ui/u2_agent_ux/app.py"""
import streamlit as st

from track4_ui.u2_agent_ux.agent_steps import (  # noqa: F401
    ApprovalGate, render_citations, run_fake_agent, summarize_step,
)

st.set_page_config(page_title="U2 Agent UX", page_icon="🤖")

if "gate" not in st.session_state:
    st.session_state.gate = ApprovalGate()

# TODO 1: a question box; on submit run the agent and walk through its events
# TODO 2: show tool steps inside st.status("Agent is working...") using summarize_step
# TODO 3: on needs_approval: store the request in the gate, show the action + args,
#         and Approve / Reject buttons. Stop the agent loop until a decision exists.
#         Hint: keep the events list and the current position in st.session_state,
#         because every button click reruns the whole script.
# TODO 4: on answer: text, footnotes = render_citations(...); show the text, then one
#         st.expander per footnote
# TODO 5: after Reject, the answer must say the email was NOT sent
