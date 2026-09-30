# S4: Meeting notes → action items (with self-correction)

**Time:** 1 to 2 evenings · **Concepts:** custom validators (`field_validator`, `model_validator`),
validation using outside context, sending the error back to the model so it fixes itself.

## The idea
Turn messy meeting notes into a list of action items. Each item needs an owner who was really at
the meeting and a due date in the right format. When the model breaks a rule, show it the exact
error and ask it to fix its answer. This "validate, then repair" loop is used in real products.

## The models you design
```
ActionItem
  task: str              (starts with a verb, max 120 characters)
  owner: str             (must be one of the attendees)
  due_date: date | None  (ISO format, not in the past compared to meeting_date)
  priority: "low" | "medium" | "high"
MeetingSummary
  meeting_date: date
  attendees: list[str]
  decisions: list[str]
  action_items: list[ActionItem]
```

## The new part: rules that need outside context
"Owner must be an attendee" can't be checked on one `ActionItem` alone; you need the attendee list.
Use a `model_validator(mode="after")` on `MeetingSummary` that checks every item's owner.
Do the same for "due date not before meeting date".

## Steps
1. Write the models and validators. Test them first, with no LLM (`tests/`).
2. Write `extract(notes)`:
   - attempt 1: normal prompt
   - if `ValidationError`: build a **repair prompt** with the notes, the model's last JSON,
     and the error message, and ask for a corrected JSON
   - stop after 3 attempts
3. Run on `data/notes_1.txt` and `data/notes_2.txt`. Print how many repairs were needed.
4. Log: which rules did the model break most?

## Done when
- [ ] Validator tests pass (owner not in attendees fails; due date before meeting fails).
- [ ] Both notes files give a valid `MeetingSummary` within 3 attempts.
- [ ] The script prints each repair attempt and the error that caused it.

## Stretch goals
- Keep a count of which validator failed most across 10 runs.
- Turn "next Friday" into a real date using `meeting_date`. Do it in Python, not in the prompt.
