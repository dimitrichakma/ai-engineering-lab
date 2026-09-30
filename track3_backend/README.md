# Track 3: Backend design

One running example through B1 to B4: a **Job Application Tracker API**. You track the jobs you
apply to, their status, and notes. Useful for your real job search, and every step builds on the last:

| Project | What changes in the same app |
| --- | --- |
| B1 API design | In memory storage, clean routes, models, errors, pagination |
| B2 Database | Same API, now stored in SQLite/Postgres with migrations |
| B3 Background jobs | Add "analyse this job post with an LLM" as a slow background job |
| B4 Multi user | Two users, each sees only their own applications |
| B5 Docker + CI | Package it, and GitHub Actions runs tests + an eval gate on every push |
| D1 Cloud deploy | Put it online for $0, provider agnostic |

Extra packages for this track: `uv add fastapi uvicorn httpx sqlalchemy alembic`
