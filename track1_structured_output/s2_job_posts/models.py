from typing import Literal

from pydantic import BaseModel, Field, model_validator


class Salary(BaseModel):
    # TODO: min_bdt, max_bdt, period (see TASK.md). Add descriptions.

    # TODO: add a model_validator(mode="after") that raises ValueError
    #       when both min_bdt and max_bdt exist and min_bdt > max_bdt.
    pass


class Requirement(BaseModel):
    # TODO: skill and required, with descriptions that explain must have vs nice to have.
    pass


class JobPost(BaseModel):
    # TODO: all JobPost fields from TASK.md.
    # Hint: a list field is list[Requirement]; an optional nested field is Salary | None.
    pass
