import pytest

from track4_ui.u1_streaming_chat.chat_logic import (
    add_message, collect_stream, new_state, retry_last, trim_history,
)


def test_add_message_and_bad_role():
    s = new_state()
    add_message(s, "user", "hi")
    assert s["messages"] == [{"role": "user", "content": "hi"}]
    with pytest.raises(ValueError):
        add_message(s, "robot", "x")


def test_trim_keeps_system_and_last_n():
    msgs = [{"role": "system", "content": "sys"}] + [
        {"role": "user", "content": str(i)} for i in range(10)
    ]
    out = trim_history(msgs, 3)
    assert out[0]["role"] == "system"
    assert [m["content"] for m in out[1:]] == ["7", "8", "9"]


def test_trim_without_system():
    msgs = [{"role": "user", "content": str(i)} for i in range(5)]
    assert [m["content"] for m in trim_history(msgs, 2)] == ["3", "4"]


def test_collect_stream_full():
    assert collect_stream(["a ", "b ", "c"], lambda: False) == ("a b c", False)


def test_collect_stream_stops_early():
    calls = {"n": 0}

    def stop():
        calls["n"] += 1
        return calls["n"] > 2

    text, stopped = collect_stream(["a ", "b ", "c ", "d"], stop)
    assert stopped is True
    assert text == "a b "


def test_retry_last():
    s = new_state()
    add_message(s, "user", "q1")
    add_message(s, "assistant", "a1")
    assert retry_last(s) == "q1"
    assert s["messages"] == [{"role": "user", "content": "q1"}]
    assert retry_last(new_state()) is None
