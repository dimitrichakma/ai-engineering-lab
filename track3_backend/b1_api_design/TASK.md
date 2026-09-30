# B1: API design

**Time:** 1 to 2 evenings · **Skill:** designing an API that is easy to use, hard to misuse, and
consistent everywhere. Your earlier projects have APIs; here you make every design choice yourself.

## Resources
```
Application: id, company, role, status, applied_on, url, created_at, updated_at
  status: saved | applied | interview | offer | rejected
Note: id, application_id, text, created_at
```

## Endpoints (all under `/v1`)
| Method | Path | Notes |
| --- | --- | --- |
| POST | /v1/applications | 201 + `Location` header |
| GET | /v1/applications | filter `?status=`, paginate `?limit=&cursor=` |
| GET | /v1/applications/{id} | 404 if missing |
| PATCH | /v1/applications/{id} | partial update; status changes must follow the allowed flow |
| DELETE | /v1/applications/{id} | 204 |
| POST | /v1/applications/{id}/notes | |
| GET | /v1/applications/{id}/notes | |

## Design rules you must follow
1. **Separate models:** `ApplicationCreate`, `ApplicationUpdate` (all optional), `ApplicationOut`.
   The client never sends `id`, `created_at` or `updated_at`.
2. **One error format everywhere:** `{"error": {"code": "not_found", "message": "...", "details": {...}}}`.
   Add exception handlers so even validation errors (422) use this shape.
3. **Status flow:** `saved → applied → interview → offer`, and any status → `rejected`.
   An invalid change returns 409 with code `invalid_transition`.
4. **Cursor pagination:** the response is `{"items": [...], "next_cursor": "..." | null}`.
   Why a cursor and not `?page=3`? Write your answer in the log.
5. **OpenAPI:** every route has a summary and response examples. Check `/docs` looks clean.

## Given
`store.py`: a simple in memory store. `app.py` has the skeleton and TODOs.

## Done when
- [ ] Tests for every endpoint pass, including 404, 409 and 422 in the common error format.
- [ ] Paging through 25 applications with `limit=10` gives 10, 10, 5 and then `next_cursor = null`.
- [ ] `/docs` shows clear summaries and examples.
