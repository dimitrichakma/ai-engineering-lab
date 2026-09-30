"""MCP client agent with an allowlist."""
import logging
from typing import Any

log = logging.getLogger(__name__)

ALLOWLIST = {"add_note", "list_notes", "search_notes"}
MAX_STEPS = 6


def filter_tools(tools: list[Any], allowlist: set[str]) -> list[Any]:
    # TODO: tools have a .name attribute. Keep allowlisted ones; log.warning the dropped names.
    raise NotImplementedError


def to_ollama_tool(tool: Any) -> dict:
    # TODO: {"type": "function", "function": {"name": tool.name,
    #        "description": tool.description or "", "parameters": tool.inputSchema}}
    raise NotImplementedError


def is_call_allowed(name: str, allowlist: set[str]) -> bool:
    # TODO: the last line of defense, checked before EVERY session.call_tool
    raise NotImplementedError


async def run_agent(question: str, allowlist: set[str] = ALLOWLIST) -> str:
    # TODO:
    # from mcp import ClientSession, StdioServerParameters
    # from mcp.client.stdio import stdio_client
    # params = StdioServerParameters(command=sys.executable,
    #          args=["-m", "track5_agentic.a5_mcp_client.notes_server"])
    # async with stdio_client(params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()
    #         tools = filter_tools((await session.list_tools()).tools, allowlist)
    #         ... C1 loop with ollama.AsyncClient().chat(..., tools=[to_ollama_tool(t) ...])
    #         result = await session.call_tool(name, args); text from result.content
    raise NotImplementedError


if __name__ == "__main__":
    import asyncio

    print(asyncio.run(run_agent("Save a note: buy tea. Then show all notes.")))
