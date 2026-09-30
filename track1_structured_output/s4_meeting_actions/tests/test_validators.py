from datetime import date

import pytest
from pydantic import ValidationError

from track1_structured_output.s4_meeting_actions.models import MeetingSummary


def base(**overrides):
    data = {
        "meeting_date": date(2026, 10, 2),
        "attendees": ["Tania", "Rafi", "Joy"],
        "decisions": ["Launch moves to 20 Oct"],
        "action_items": [
            {"task": "Finish gateway testing", "owner": "Rafi",
             "due_date": date(2026, 10, 10), "priority": "high"},
        ],
    }
    data.update(overrides)
    return data


def test_valid_summary():
    MeetingSummary(**base())


def test_owner_must_be_attendee():
    items = [{"task": "Email designer", "owner": "Karim", "due_date": None, "priority": "low"}]
    with pytest.raises(ValidationError) as exc:
        MeetingSummary(**base(action_items=items))
    assert "Karim" in str(exc.value)


# TODO: test that a due_date before meeting_date fails.
# TODO: test that owner matching ignores case ("rafi" is fine).
# TODO: test that a 200 character task fails.
