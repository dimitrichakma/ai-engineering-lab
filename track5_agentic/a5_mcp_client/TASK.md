# A5: MCP client

**Time:** 1 to 2 evenings · **Skill:** connecting your agent to tools through the Model Context
Protocol, so tools can live in separate programs (yours or someone else's).

## The idea
In C1 your tools were Python functions in the same file. With MCP, a **server** offers tools and a
**client** (your agent) discovers them at run time: names, descriptions, input schemas. The risk:
a server can offer more tools than you want, or change them later. So the client **allowlists**.

## Given
`notes_server.py`: a tiny MCP server (FastMCP) with `add_note`, `list_notes`, `search_notes`
and `delete_all_notes` (the dangerous one). Run it alone: `uv run python -m track5_agentic.a5_mcp_client.notes_server`

## What you write in `client.py`
1. `filter_tools(tools, allowlist) -> list`: keep only allowlisted names; log the ones dropped.
2. `to_ollama_tool(tool) -> dict`: convert an MCP tool (name, description, inputSchema) to the
   `{"type": "function", "function": {...}}` format Ollama expects.
3. `async run_agent(question, allowlist)`: start the server over **stdio**, `initialize`,
   `list_tools`, filter, give the tools to Ollama, and run the C1 style loop, calling
   `session.call_tool(name, args)`. Refuse (don't call) any tool name not in the allowlist, even if
   the model asks for it. Step limit: 6.

Read the current Python SDK README first: https://github.com/modelcontextprotocol/python-sdk

## Done when
- [ ] `uv run pytest track5_agentic/a5_mcp_client` passes.
- [ ] "Save a note: buy tea, then show all notes" works with the real model.
- [ ] `delete_all_notes` is never offered to the model, and a forced call to it is refused.
- [ ] Bonus: connect your habit tracker MCP server as a second server with its own allowlist.
