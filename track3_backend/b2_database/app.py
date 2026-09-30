"""Copy your finished B1 routes here and replace the in memory store with the database session.

Run: uv run uvicorn track3_backend.b2_database.app:app --reload
"""
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import get_session

app = FastAPI(title="Job Application Tracker (database)", version="1.1.0")

# TODO: models + error handlers from B1
# TODO: routes from B1, each with `session: Session = Depends(get_session)`
# TODO: GET /v1/applications?include=notes  (slow version first, then selectinload)
_ = (Depends, Session, get_session)
