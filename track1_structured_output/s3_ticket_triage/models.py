from typing import Literal

from pydantic import BaseModel, Field

Category = Literal["delivery", "payment", "refund", "product_issue", "account", "other"]
Urgency = Literal["low", "medium", "high"]
Language = Literal["english", "bangla", "banglish"]


class Triage(BaseModel):
    # TODO: category, urgency, language, summary (see TASK.md), each with a description.
    # Tip: the descriptions of category values matter a lot. Try with and without them.
    pass
