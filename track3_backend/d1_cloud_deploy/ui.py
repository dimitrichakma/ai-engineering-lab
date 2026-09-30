"""Streamlit UI for the deployed API.
Local:  API_URL=http://localhost:8000 uv run streamlit run track3_backend/d1_cloud_deploy/ui.py
Cloud:  set API_URL (and API key if B4) in Streamlit Community Cloud secrets."""
import os

import httpx
import streamlit as st

API_URL = os.getenv("API_URL") or st.secrets.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Job Application Tracker", page_icon="📋")
st.title("Job Application Tracker")
st.caption("Demo app. The free server sleeps when idle, so the first load can take ~1 minute.")

# TODO 1: a form to add an application (company, role, url) -> POST /v1/applications
# TODO 2: a table of applications -> GET /v1/applications (show status with a colour)
# TODO 3: a select box to change status -> PATCH; show the API's error message nicely on 409
# TODO 4: handle the API being asleep or down: a friendly message + a retry button, never a traceback
_ = httpx
