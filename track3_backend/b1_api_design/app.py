"""Run: uv run uvicorn track3_backend.b1_api_design.app:app --reload"""
from datetime import date, datetime
from typing import Literal

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from . import store

Status = Literal["saved", "applied", "interview", "offer", "rejected"]

ALLOWED = {
    "saved": {"applied", "rejected"},
    "applied": {"interview", "rejected"},
    "interview": {"offer", "rejected"},
    "offer": {"rejected"},
    "rejected": set(),
}

app = FastAPI(title="Job Application Tracker", version="1.0.0")


class ApiError(Exception):
    def __init__(self, status_code: int, code: str, message: str, details: dict | None = None):
        self.status_code, self.code, self.message, self.details = status_code, code, message, details or {}


# ---------- models ----------
class ApplicationCreate(BaseModel):
    # TODO: company (1..100 chars), role, status (default "saved"), applied_on (date | None), url (str | None)
    pass


class ApplicationUpdate(BaseModel):
    # TODO: every field optional
    pass


class ApplicationOut(BaseModel):
    # TODO: all fields incl. id, created_at, updated_at
    pass


class Page(BaseModel):
    items: list[ApplicationOut]
    next_cursor: str | None


# ---------- error handlers ----------
@app.exception_handler(ApiError)
async def api_error_handler(request: Request, exc: ApiError):
    # TODO: return JSONResponse(status_code=..., content={"error": {"code", "message", "details"}})
    raise NotImplementedError


@app.exception_handler(RequestValidationError)
async def validation_handler(request: Request, exc: RequestValidationError):
    # TODO: same shape, status 422, code "validation_error", details = exc.errors()
    raise NotImplementedError


# ---------- routes ----------
# TODO: POST   /v1/applications              -> 201, Location header
# TODO: GET    /v1/applications              -> Page; ?status= ; ?limit=10 (1..100) ; ?cursor=
#        (hint: the cursor can simply be the last id you returned, as a string)
# TODO: GET    /v1/applications/{app_id}     -> 404 ApiError("not_found") if missing
# TODO: PATCH  /v1/applications/{app_id}     -> check ALLOWED for status changes, 409 "invalid_transition"
# TODO: DELETE /v1/applications/{app_id}     -> 204
# TODO: POST/GET /v1/applications/{app_id}/notes
_ = (date, datetime, Field, store)
