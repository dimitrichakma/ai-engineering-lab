"""Tests with a FAKE model, so they are fast, free and repeatable."""
from types import SimpleNamespace as NS

from track2_core.c1_tool_calling import store
from track2_core.c1_tool_calling.agent_loop import run_turn
from track2_core.c1_tool_calling.tools import TOOL_SCHEMAS, run_tool


def call(name, **args):
    return NS(function=NS(name=name, arguments=args))


def scripted_model(*steps):
    """Returns a chat_fn that plays back `steps` in order.
    Each step is either a list of tool calls or a final text string."""
    it = iter(steps)

    def chat_fn(messages, tools):
        step = next(it)
        if isinstance(step, str):
            return NS(message=NS(role="assistant", content=step, tool_calls=None))
        return NS(message=NS(role="assistant", content="", tool_calls=step))
    return chat_fn


def setup_function():
    store.reset()


def test_two_tool_calls_then_answer():
    model = scripted_model([call("add_book", title="Atomic Habits"),
                            call("log_pages", title="Atomic Habits", pages=30)],
                           "Added it and logged 30 pages.")
    reply, called = run_turn(1, "add and log", chat_fn=model)
    assert called == ["add_book", "log_pages"]
    assert store.BOOKS[1]["Atomic Habits"] == 30


def test_schemas_never_mention_user_id():
    assert "user_id" not in str(TOOL_SCHEMAS)


def test_unknown_tool_returns_error_string():
    assert "Unknown tool" in run_tool("delete_everything", {}, user_id=1)


# TODO: test that max_steps stops a model that calls reading_summary forever
#       (hint: a chat_fn that ALWAYS returns a tool call, no scripted end)
# TODO: test that user 1 asking for "user 2's books" never sees "Secret Diary"
#       (hint: the fake model calls reading_summary; check the tool result in the messages
#        or the store access, whatever your design allows)
# TODO: test run_tool with a missing argument returns "Bad arguments ..."
