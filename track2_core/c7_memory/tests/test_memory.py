from track2_core.c7_memory.memory import SummaryMemory, count_tokens, trim_history


def msg(role, n_chars):
    return {"role": role, "content": "x" * n_chars}


def test_count_tokens_rounds_up():
    assert count_tokens("abcde") == 2


def test_trim_keeps_system_and_newest():
    history = [msg("system", 400), msg("user", 40), msg("assistant", 40),
               msg("user", 40), msg("assistant", 40)]
    out = trim_history(history, max_tokens=30)   # each non-system msg = 10 + 4 = 14 tokens
    assert out[0]["role"] == "system"
    assert len(out) == 3                          # system + last user + last assistant


def test_trim_never_starts_on_assistant_or_tool():
    history = [msg("user", 40), msg("assistant", 40), msg("tool", 40), msg("assistant", 40)]
    out = trim_history(history, max_tokens=45)
    assert out == [] or out[0]["role"] == "user"


def test_summary_memory_folds_old_messages():
    folded = []

    def fake_summarize(old, msgs):
        folded.extend(msgs)
        return (old + " | " if old else "") + f"{len(msgs)} msgs"

    mem = SummaryMemory("sys", max_recent_tokens=30, summarize_fn=fake_summarize)
    for i in range(3):
        mem.add(msg("user", 40))
        mem.add(msg("assistant", 40))
    ctx = mem.context()
    assert ctx[0]["content"] == "sys"
    assert "msgs" in ctx[1]["content"]
    assert len(folded) >= 2


# TODO: a message bigger than max_tokens on its own: what should trim_history return? Decide, test it.
# TODO: context() has no summary message before anything is folded
