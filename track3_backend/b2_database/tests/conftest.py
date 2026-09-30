"""Point the app at a fresh temporary SQLite database for every test.

Finish db.py and models.py first; then this fixture works as is."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def client(tmp_path):
    from track3_backend.b2_database.app import app
    from track3_backend.b2_database.db import get_session
    from track3_backend.b2_database.models import Base

    engine = create_engine(f"sqlite:///{tmp_path / 'test.db'}")
    Base.metadata.create_all(engine)      # fine in TESTS; production uses Alembic
    TestSession = sessionmaker(bind=engine, expire_on_commit=False)

    def override():
        s = TestSession()
        try:
            yield s
            s.commit()
        except Exception:
            s.rollback()
            raise
        finally:
            s.close()

    app.dependency_overrides[get_session] = override
    yield TestClient(app)
    app.dependency_overrides.clear()
