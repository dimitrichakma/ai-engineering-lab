import os
from typing import Iterator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tracker.db")

# TODO: engine = create_engine(DATABASE_URL, echo=os.getenv("SQL_ECHO") == "1")
# TODO: SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_session() -> Iterator[Session]:
    """FastAPI dependency: one session per request.
    Commit if the request succeeded, roll back if anything raised, always close."""
    # TODO
    raise NotImplementedError
