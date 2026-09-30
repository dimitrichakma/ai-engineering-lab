from typing import Literal

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    # TODO: add every field from the table in TASK.md.
    # Use Field(description="...") on each one. Example of the pattern (a different field):
    #     currency: Literal["BDT"] = Field(description="Currency of the amount. Always BDT.")
    # TODO: make amount_bdt reject 0 and negative values (hint: Field has gt=).
    pass
