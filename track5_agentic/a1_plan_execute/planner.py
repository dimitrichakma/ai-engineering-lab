"""Plan and execute with replanning."""
from collections.abc import Callable
from typing import Any

from pydantic import BaseModel, Field


class Step(BaseModel):
    id: int
    tool: str
    args: dict[str, Any] = Field(default_factory=dict)
    depends_on: list[int] = Field(default_factory=list)


class Plan(BaseModel):
    goal: str
    steps: list[Step]


class RunResult(BaseModel):
    status: str  # "done" | "failed"
    results: dict[int, Any]
    replans: int
    errors: list[str] = Field(default_factory=list)


Tools = dict[str, Callable[..., Any]]
Replan = Callable[[Plan, Step, str, dict[int, Any]], Plan]


def resolve_args(args: dict[str, Any], results: dict[int, Any]) -> dict[str, Any]:
    """Given. "$3" becomes the result of step 3."""
    out = {}
    for k, v in args.items():
        if isinstance(v, str) and v.startswith("$") and v[1:].isdigit():
            out[k] = results[int(v[1:])]
        else:
            out[k] = v
    return out


def validate_plan(plan: Plan, tools: Tools) -> list[str]:
    # TODO: unknown tool, duplicate ids, missing dependency, cycle
    raise NotImplementedError


def order_steps(plan: Plan) -> list[Step]:
    # TODO: topological sort (Kahn's algorithm). Assume the plan is valid.
    raise NotImplementedError


def execute(plan: Plan, tools: Tools, replan: Replan, max_replans: int = 2) -> RunResult:
    # TODO: see TASK.md step 3. Skip steps whose id is already in results after a replan.
    raise NotImplementedError


def make_plan(goal: str, tools: Tools, llm: Callable[[str, dict], str]) -> Plan:
    # TODO: prompt = goal + tool names and their docstrings; llm(prompt, Plan.model_json_schema())
    #       parse with Plan.model_validate_json; retry once with the validation errors (Track 1 S2)
    raise NotImplementedError
