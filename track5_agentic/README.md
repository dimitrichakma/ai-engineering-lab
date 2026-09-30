# Track 5: Agentic AI

Agents that plan, split work, wait for a human, run code, use MCP tools, get evaluated, and
survive attacks hidden in the data they read. None of these depend on your earlier projects.

| Project | Skill | Core? |
| --- | --- | --- |
| A1 plan and execute | a checked plan, then execution with replanning on failure | ⭐ |
| A2 orchestrator + workers + critic | split a task, run workers in parallel, review the result | |
| A3 human in the loop + durable runs | pause for approval, survive a restart (LangGraph) | ⭐ |
| A4 code running agent | run model written code in a limited subprocess | |
| A5 MCP client | discover tools from an MCP server, allowlist them | |
| A6 agent evaluation | success rate, trajectory checks, steps and cost | ⭐ |
| A7 indirect prompt injection | attacks hidden in tool results, and defenses | ⭐ |

## Rules
- Every agent has a **step limit** and a **time limit**. No infinite loops.
- The model never gets a tool you haven't allowlisted.
- Anything that changes the world (send, delete, pay) needs approval (see U2, A3, A7).
- Tests use fake LLMs and fake tools, so they run without Ollama. Try the real model after.
- Only A3 uses LangGraph. Everything else is plain Python, so you see how agents really work.
