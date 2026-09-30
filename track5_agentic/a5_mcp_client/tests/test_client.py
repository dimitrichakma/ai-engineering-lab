from types import SimpleNamespace

from track5_agentic.a5_mcp_client.client import (
    ALLOWLIST, filter_tools, is_call_allowed, to_ollama_tool,
)


def tool(name, desc="d"):
    return SimpleNamespace(name=name, description=desc,
                           inputSchema={"type": "object", "properties": {"text": {"type": "string"}}})


def test_filter_drops_dangerous_tool(caplog):
    tools = [tool("add_note"), tool("delete_all_notes"), tool("list_notes")]
    kept = [t.name for t in filter_tools(tools, ALLOWLIST)]
    assert kept == ["add_note", "list_notes"]
    assert "delete_all_notes" in caplog.text


def test_ollama_format():
    t = to_ollama_tool(tool("add_note", "Save a note"))
    assert t["type"] == "function"
    assert t["function"]["name"] == "add_note"
    assert t["function"]["parameters"]["properties"]["text"]["type"] == "string"


def test_none_description_becomes_empty():
    assert to_ollama_tool(tool("x", None))["function"]["description"] == ""


def test_call_guard():
    assert is_call_allowed("add_note", ALLOWLIST)
    assert not is_call_allowed("delete_all_notes", ALLOWLIST)
