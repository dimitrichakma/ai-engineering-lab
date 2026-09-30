import asyncio
import json
import time

from track5_agentic.a2_orchestrator_workers.orchestrator import (
    MAX_SUBTASKS, Review, Subtask, review_loop, run_workers, split_task,
)


def test_split_task_caps_subtasks():
    fake = lambda prompt, schema: json.dumps(
        {"subtasks": [{"id": i, "instruction": f"part {i}"} for i in range(9)]}
    )
    assert len(split_task("job", fake)) == MAX_SUBTASKS


def test_workers_run_in_parallel_and_survive_failure():
    async def worker(st: Subtask) -> str:
        await asyncio.sleep(0.2)
        if st.id == 2:
            raise RuntimeError("boom")
        return f"done {st.id}"

    subs = [Subtask(id=i, instruction="x") for i in range(1, 5)]
    t = time.perf_counter()
    res = asyncio.run(run_workers(subs, worker, limit=4))
    assert time.perf_counter() - t < 0.5
    assert [r.subtask_id for r in res] == [1, 2, 3, 4]
    assert res[1].ok is False and "boom" in res[1].error
    assert res[0].text == "done 1"


def test_semaphore_limits_concurrency():
    running = {"now": 0, "max": 0}

    async def worker(st):
        running["now"] += 1
        running["max"] = max(running["max"], running["now"])
        await asyncio.sleep(0.05)
        running["now"] -= 1
        return "ok"

    asyncio.run(run_workers([Subtask(id=i, instruction="x") for i in range(6)], worker, limit=2))
    assert running["max"] == 2


def test_review_loop_uses_feedback():
    seen = []

    def draft(feedback):
        seen.append(feedback)
        return "v2 with sources" if feedback else "v1"

    critic = lambda text: Review(ok="sources" in text, feedback="add sources")
    out = review_loop(draft, critic, max_rounds=3)
    assert out.approved and out.rounds == 2
    assert seen == ["", "add sources"]


def test_review_loop_stops_at_max():
    out = review_loop(lambda fb: "bad", lambda t: Review(ok=False, feedback="no"), max_rounds=2)
    assert not out.approved and out.rounds == 2
