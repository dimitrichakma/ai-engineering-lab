# B2: Database + migrations

**Time:** 1 to 2 evenings · **Skill:** storing data properly: SQLAlchemy 2.0 models, sessions,
transactions, Alembic migrations, indexes, and the "N+1 query" problem.

## The idea
Keep the B1 API exactly the same from the outside, but store data in a real database.
Use SQLite locally (a file, free). The same code runs on Postgres later by changing `DATABASE_URL`.

## Steps
1. `models.py`: SQLAlchemy 2.0 typed models (`Mapped[...]`, `mapped_column`) for `Application` and `Note`,
   with a relationship and `ON DELETE CASCADE` for notes.
2. `db.py`: engine from `DATABASE_URL` (default `sqlite:///./tracker.db`), `SessionLocal`, and a
   FastAPI dependency `get_session()` that commits on success and rolls back on error.
3. **Alembic:** `uv run alembic init migrations`, point it at your models, create the first
   migration with `--autogenerate`, read the generated file, then `alembic upgrade head`.
4. **Second migration:** add a `salary_bdt` column (nullable). This is how real schemas change.
5. **Index:** add an index on `(status, created_at)`. Explain in the log which query it speeds up.
6. Copy your B1 routes into `app.py` and switch them from `store` to the session.
7. **N+1:** add `GET /v1/applications?include=notes`. First write it the slow way (one query per
   application). Turn on SQL logging (`echo=True`) and count the queries for 20 applications.
   Then fix it with `selectinload` and count again.

## Done when
- [ ] The B1 tests pass against this app with a temporary SQLite file (see `tests/conftest.py`).
- [ ] Two migrations exist and `alembic downgrade -1` then `upgrade head` both work.
- [ ] Your log shows the query count before and after the N+1 fix.

## Questions for your log
- Why should a failed request roll back? What could be left half written otherwise?
- Why use migrations instead of `Base.metadata.create_all()` in production?
