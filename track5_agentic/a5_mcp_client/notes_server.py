"""Given. A tiny MCP server over stdio. Notes live in memory while the server runs."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("notes")
NOTES: list[str] = []


@mcp.tool()
def add_note(text: str) -> str:
    """Save a short note."""
    NOTES.append(text)
    return f"saved note #{len(NOTES)}"


@mcp.tool()
def list_notes() -> list[str]:
    """Return all notes."""
    return NOTES


@mcp.tool()
def search_notes(query: str) -> list[str]:
    """Return notes that contain the query (case insensitive)."""
    return [n for n in NOTES if query.lower() in n.lower()]


@mcp.tool()
def delete_all_notes() -> str:
    """Delete every note. Dangerous: the client must NOT allowlist this."""
    NOTES.clear()
    return "all notes deleted"


if __name__ == "__main__":
    mcp.run()  # stdio by default
