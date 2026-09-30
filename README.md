# AI Engineering Lab

35 small projects in 6 tracks that build the skills behind a real AI product: structured output,
agents, retrieval, evals, safety, backend, UI, deployment and model choice.

You write the code yourself. Every project has a `TASK.md`, starter code with `TODO`s, and tests.
Everything runs free on your laptop with Ollama. The only cloud parts (D1, M3) are $0 and need no card.

## The tracks

| Track | Projects | What you learn |
| --- | --- | --- |
| 1 Structured output | S0 setup, S1 to S5 ⭐ | JSON that follows a schema, validation, repair, an extraction API |
| 2 Core patterns | C1 ⭐ tool calling, C2 guardrails, C3 gateway, C4 ⭐ evals, C5 ⭐ reliability, C6 ⭐ retrieval, C7 memory, C8 async, C9 caching, C10 ⭐ observability, C11 ⭐ doc ingestion | the patterns inside every AI app |
| 3 Backend + deploy | B1 ⭐ API design, B2 ⭐ database, B3 background jobs, B4 multi user, B5 ⭐ Docker + CI, D1 ⭐ cloud deploy | a real API around an AI feature, shipped safely |
| 4 UI (Streamlit) | U1 ⭐ streaming chat, U2 ⭐ agent UX, U3 eval dashboard | an AI app that feels good and shows its work |
| 5 Agentic | A1 ⭐ plan and execute, A2 orchestrator, A3 ⭐ human in the loop, A4 code agent, A5 MCP client, A6 ⭐ agent eval, A7 ⭐ prompt injection | agents that are useful, measured and safe |
| 6 Models | M1 model selection, M2 embeddings, M3 LoRA fine tune | picking and adapting models with evidence |

⭐ = core (21 projects). Do these first; the rest when a real project needs them.
`worksheets/`: 5 no code worksheets about your own projects. One a week, no AI help.

## Suggested order
1. Track 1 (S0 → S5)
2. C1 → C4 → C5
3. B1 → B2
4. C11 → C6
5. U1 → U2
6. A1 → A3 → A6 → A7
7. C10 → B5 → D1
8. Track 6, then the non core projects as you need them

## Setup (once)
1. Install [uv](https://docs.astral.sh/uv/) and [Ollama](https://ollama.com).
2. Models: `ollama pull qwen2.5:3b` and `ollama pull nomic-embed-text` (M1 and M2 add more later).
3. In this folder:
   ```bash
   uv init --python 3.13
   uv add pydantic ollama python-dotenv pytest httpx pandas rank-bm25 pdfplumber streamlit \
          fastapi uvicorn sqlalchemy alembic langgraph langgraph-checkpoint-sqlite mcp
   cp .env.example .env
   ```
4. Do `track1_structured_output/S0_SETUP.md` first. It builds `common/llm.py`, used everywhere.
5. Read `COST_SAFETY.md` before D1 or M3.

## How to work on each project
1. Read `TASK.md` fully.
2. Write the smallest version that works. Run its tests, for example
   `uv run pytest track2_core/c9_caching`
3. Try it with the real model, and write the numbers and lessons in `LEARNING_LOG.md`.
4. Commit.

Tests use fake models, so they pass without Ollama. A test failing with `NotImplementedError`
just means the TODO is still waiting for you.

## Rules for using Claude
- ✅ Explain a concept or an error. Give a hint. Review your code after it works.
- ❌ Write the TODO code for you.

`CLAUDE.md` puts Claude Code in tutor mode. Stuck for 30 minutes? Ask for a bigger hint, not the answer.
