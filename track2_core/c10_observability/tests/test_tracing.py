import pytest

from track2_core.c10_observability.tracing import new_trace, span


def test_nested_spans_get_parent_ids():
    records = []
    new_trace()
    with span("outer", sink=records.append):
        with span("inner", sink=records.append):
            pass
    inner, outer = records            # inner finishes first
    assert inner["parent_id"] == outer["span_id"]
    assert outer["parent_id"] is None
    assert inner["trace_id"] == outer["trace_id"]


def test_error_is_recorded_and_raised():
    records = []
    new_trace()
    with pytest.raises(ValueError):
        with span("boom", sink=records.append):
            raise ValueError("bad")
    assert records[0]["status"] == "error"
    assert "bad" in records[0]["error"]

# TODO: attrs set with current_span().set(...) appear in the record
# TODO: duration_ms is a positive number
