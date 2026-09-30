# B4: Multi user data access

**Time:** 1 to 2 evenings · **Skill:** making sure one user can never read or change another
user's data. This is the most common serious bug in real apps ("broken object level
authorization", number 1 on the OWASP API Security Top 10).

## The idea
Take your B2 app and add users. For learning, auth is simple: each user has an API key sent in
the `X-API-Key` header. (Somajji uses Google sign in; the scoping rules below are the same.)

## Rules
1. The user id comes ONLY from the verified API key, never from the URL, body or query.
2. EVERY query on `applications` and `notes` filters by `owner_id`. No exceptions.
3. Asking for another user's application returns **404, not 403**. Why? (Write it in the log.)
4. Put the scoping in ONE place (a helper like `get_owned_application(session, user, app_id)`),
   so a new route can't forget it.

## What you write
1. `users` table with `id`, `name`, `api_key_hash` (store a hash, never the raw key).
2. `current_user` dependency: reads `X-API-Key`, hashes it, looks it up, 401 if missing or wrong.
3. `owner_id` on applications (a new Alembic migration).
4. Update every route to use `current_user` and the scoping helper.
5. `seed.py`: creates two users, Rina and Arif, and prints their API keys once.

## Done when
- [ ] The attack tests pass: Arif can't GET, PATCH, DELETE or add notes to Rina's application,
      and Arif's list never contains Rina's items.
- [ ] No API key or a wrong key → 401.
- [ ] Raw API keys are nowhere in the database.

## Question for your log
Worksheet 3 asks how your habit tracker scopes tools by `thread_id`. How is that the same idea?
