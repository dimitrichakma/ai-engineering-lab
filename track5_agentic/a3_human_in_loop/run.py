"""CLI for durable runs. Paused runs are saved in runs.db and survive closing the terminal.

uv run python -m track5_agentic.a3_human_in_loop.run start "Please refund 1200 taka"
uv run python -m track5_agentic.a3_human_in_loop.run list
uv run python -m track5_agentic.a3_human_in_loop.run approve <thread_id>
uv run python -m track5_agentic.a3_human_in_loop.run reject <thread_id> "be kinder"
"""
import sys  # noqa: F401

# TODO 1: from langgraph.checkpoint.sqlite import SqliteSaver
#         with SqliteSaver.from_conn_string("runs.db") as saver: app = build_graph(saver, llm)
# TODO 2: start: new thread_id (uuid4), invoke, print the draft and the thread id
# TODO 3: list: keep your own small table of thread ids (or read them from the saver),
#         and show the ones whose app.get_state(config).next is not empty (still paused)
# TODO 4: approve / reject: app.invoke(Command(resume=...), config)
