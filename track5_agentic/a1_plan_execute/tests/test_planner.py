from track5_agentic.a1_plan_execute.planner import (
    Plan, Step, execute, order_steps, validate_plan,
)

TOOLS = {
    "get_price": lambda item: {"tea": 50, "coffee": 120}[item],
    "double": lambda x: x * 2,
    "flaky": lambda x: (_ for _ in ()).throw(RuntimeError("service down")),
}


def plan(*steps):
    return Plan(goal="g", steps=[Step(**s) for s in steps])


def test_validate_finds_problems():
    p = plan(
        {"id": 1, "tool": "nope"},
        {"id": 2, "tool": "double", "depends_on": [9]},
        {"id": 3, "tool": "double", "depends_on": [4]},
        {"id": 4, "tool": "double", "depends_on": [3]},
    )
    problems = " ".join(validate_plan(p, TOOLS)).lower()
    assert "nope" in problems
    assert "9" in problems
    assert "cycle" in problems


def test_valid_plan_has_no_problems():
    p = plan({"id": 1, "tool": "get_price", "args": {"item": "tea"}})
    assert validate_plan(p, TOOLS) == []


def test_order_respects_dependencies():
    p = plan(
        {"id": 2, "tool": "double", "depends_on": [1]},
        {"id": 1, "tool": "get_price"},
    )
    assert [s.id for s in order_steps(p)] == [1, 2]


def test_execute_with_references():
    p = plan(
        {"id": 1, "tool": "get_price", "args": {"item": "tea"}},
        {"id": 2, "tool": "double", "args": {"x": "$1"}, "depends_on": [1]},
    )
    r = execute(p, TOOLS, replan=lambda *a: None)
    assert r.status == "done"
    assert r.results == {1: 50, 2: 100}


def test_replan_after_failure_keeps_results():
    p = plan(
        {"id": 1, "tool": "get_price", "args": {"item": "coffee"}},
        {"id": 2, "tool": "flaky", "args": {"x": "$1"}, "depends_on": [1]},
    )
    calls = []

    def replan(old, failed, error, results):
        calls.append((failed.id, error))
        return plan(
            {"id": 1, "tool": "get_price", "args": {"item": "coffee"}},
            {"id": 3, "tool": "double", "args": {"x": "$1"}, "depends_on": [1]},
        )

    r = execute(p, TOOLS, replan)
    assert r.status == "done"
    assert r.replans == 1
    assert r.results[3] == 240
    assert calls[0][0] == 2 and "service down" in calls[0][1]


def test_gives_up_after_max_replans():
    p = plan({"id": 1, "tool": "flaky", "args": {"x": 1}})
    r = execute(p, TOOLS, replan=lambda old, *a: old, max_replans=2)
    assert r.status == "failed"
    assert r.replans == 2
