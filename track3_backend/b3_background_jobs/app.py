"""Run: uv run uvicorn track3_backend.b3_background_jobs.app:app --reload"""
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from .jobs import JobStore

app = FastAPI(title="Jobs API")
store = JobStore()


class JobRequest(BaseModel):
    kind: str
    input: dict


# TODO: POST /v1/jobs -> 202, uses the Idempotency-Key header
#       (hint: idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"))
# TODO: GET /v1/jobs/{job_id} -> 404 if missing
_ = (Header, HTTPException, JobRequest)
