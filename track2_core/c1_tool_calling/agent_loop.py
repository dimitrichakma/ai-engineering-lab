"""The agent loop, written by hand."""
from typing import Callable

from .tools import TOOL_SCHEMAS, run_tool

SYSTEM = (
    "You help the user track the books they read. Use the tools to add books, log pages and "
    "show a summary. Never make up numbers; call a tool to get them."
)

# chat_fn(messages, tools) -> an object with .message.content and .message.tool_calls
ChatFn = Callable[[list[dict], list[dict]], object]


def ollama_chat(messages: list[dict], tools: list[dict]):
    import ollama
    return ollama.chat(model="qwen2.5:3b", messages=messages, tools=tools,
                       options={"temperature": 0})


def run_turn(user_id: int, user_message: str, chat_fn: ChatFn = ollama_chat,
             max_steps: int = 5) -> tuple[str, list[str]]:
    """Return (final reply text, names of the tools that were called)."""
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_message}]
    called: list[str] = []
    # TODO 1: loop at most max_steps times:
    #   resp = chat_fn(messages, TOOL_SCHEMAS)
    #   append resp.message to messages (as a dict: role "assistant", content, tool_calls)
    #   if there are no tool_calls -> return (resp.message.content, called)
    #   else for each call: result = run_tool(name, arguments, user_id)   <- user_id from HERE
    #        append {"role": "tool", "content": result, "tool_name": name}; record the name
    # TODO 2: after max_steps, return a safe message like
    #   "Sorry, I couldn't finish that. Please try a simpler request." and the called list
    raise NotImplementedError


if __name__ == "__main__":
    reply, tools_used = run_turn(1, "Add the book Atomic Habits and log 30 pages of it.")
    print("tools:", tools_used)
    print("reply:", reply)
