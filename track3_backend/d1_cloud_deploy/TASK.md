# D1: Cloud deployment ($0, provider agnostic)

**Time:** 1 to 2 evenings · **Skill:** putting an AI app online so anyone can use it, without
locking yourself to one cloud, and **without any chance of a surprise bill.**

> Read `COST_SAFETY.md` at the lab root BEFORE this project. Every step here follows it.

## The idea
One app, packaged once (your B5 Docker image), running in more than one place without code changes.
- **Backend:** your B2/B4 API in the B5 Docker image.
- **UI:** a small Streamlit app (`ui.py`) that calls the API.
- **LLM:** `LLM_PROVIDER` from the environment. Free hosting can't run Ollama (not enough memory),
  so in the cloud use `gemini` with a free tier key from a Google account with **no billing
  account attached**, or `fake` for a demo that can never cost anything.

## Where to deploy (all free, no credit card, checked September 2026)
| Part | Platform | Why |
| --- | --- | --- |
| API (Docker) | Render free web service | No card needed. Sleeps after 15 min idle (first request is slow). 750 free hours/month |
| UI (Streamlit) | Streamlit Community Cloud | Free, deploys from a public GitHub repo |
| Local "production" run | `docker compose` (from B5) | Proves the same image runs anywhere |

Free tiers change often. Before you start, open each platform's pricing page and confirm "no card
required". **If a platform asks for a card, stop and choose another one.**
(Hugging Face Docker Spaces need a paid PRO plan since July 2026, so they're not on this list.)

## Steps
1. **Make the app cloud ready** (this is the portable part):
   - read `PORT`, `DATABASE_URL`, `LLM_PROVIDER` and keys from environment variables only
   - `/health` returns 200 without calling the LLM or doing heavy work
   - logs go to stdout; no files needed to run
   - keep the C3 gateway daily cap ON in the cloud (for example 200 requests/day in total)
2. **Database:** use SQLite inside the container for the demo and accept that data resets on each
   deploy, or a free Postgres whose free tier needs no card. Write your choice in `DEPLOY.md`.
3. **Deploy the API** to Render from your GitHub repo using the Dockerfile. Put secrets in Render's
   environment settings, never in the repo.
4. **Deploy the UI** (`ui.py`) to Streamlit Community Cloud. Put `API_URL` in its secrets.
5. **Portability proof:** write `DEPLOY.md` explaining exactly what you would change to move the
   API to another platform (Railway, Cloud Run, a VPS). The answer should be "only settings".
6. **Teardown drill:** fill in `TEARDOWN.md`, then actually delete the Render service once and
   redeploy it, so you know you can.

## Done when
- [ ] A public URL shows your Streamlit UI, which talks to your API on Render.
- [ ] No secret is in the repo or the image (`git log -p | grep -i key` finds nothing real).
- [ ] The app works with `LLM_PROVIDER=fake` if the Gemini quota runs out.
- [ ] `DEPLOY.md` and `TEARDOWN.md` are filled in, and you checked the billing page of every
      platform the day after (it should say $0).

## Questions for your log
- What makes an app portable between clouds? What would lock it to one provider?
- The free API sleeps after 15 minutes. How would you explain that to a recruiter who clicks your demo?
