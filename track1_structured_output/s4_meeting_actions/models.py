from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator


class ActionItem(BaseModel):
    # TODO: task, owner, due_date, priority (see TASK.md)

    # TODO: field_validator on "task": strip spaces; raise ValueError if longer than 120 chars.
    pass


class MeetingSummary(BaseModel):
    # TODO: meeting_date, attendees, decisions, action_items

    # TODO: model_validator(mode="after") that raises ValueError with a CLEAR message when:
    #   - an action item's owner is not in attendees
    #     (compare in lowercase; the message should name the bad owner and list valid names)
    #   - an action item's due_date is before meeting_date
    # Clear error messages matter: the model will read them in the repair prompt.
    pass
