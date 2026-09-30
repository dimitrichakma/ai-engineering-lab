import os
import sys

import pytest

from track5_agentic.a4_code_agent.agent import answer
from track5_agentic.a4_code_agent.sandbox import MAX_OUTPUT, run_code


def test_runs_and_captures(tmp_path):
    r = run_code("print(6 * 7)", tmp_path)
    assert r.ok and r.stdout.strip() == "42"


def test_error_is_reported(tmp_path):
    r = run_code("1/0", tmp_path)
    assert not r.ok and "ZeroDivisionError" in r.stderr


def test_timeout(tmp_path):
    r = run_code("while True: pass", tmp_path, timeout_s=1)
    assert r.timed_out and not r.ok


def test_no_secrets_in_env(tmp_path, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "secret123")
    r = run_code("import os; print(os.environ.get('GEMINI_API_KEY'))", tmp_path)
    assert "secret123" not in r.stdout


def test_output_is_cut(tmp_path):
    r = run_code("print('x' * 100000)", tmp_path)
    assert len(r.stdout) <= MAX_OUTPUT


@pytest.mark.skipif(sys.platform != "linux", reason="RLIMIT_AS only enforced on Linux")
def test_memory_limit(tmp_path):
    r = run_code("x = bytearray(2 * 1024 * 1024 * 1024)", tmp_path, memory_mb=512)
    assert not r.ok


def test_agent_fixes_its_error():
    data = os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv")
    replies = iter([
        "import pandas as pd\nprint(pd.read_csv('data.csv')['nope'].sum())",
        "import pandas as pd\nprint(len(pd.read_csv('data.csv')))",
    ])
    out = answer("How many rows?", data, lambda prompt, system: next(replies))
    assert out["attempts"] == 2
    assert out["answer"].isdigit()
