"""Run model written Python with limits. NOT a security sandbox (see TASK.md)."""
import os  # noqa: F401
import subprocess  # noqa: F401
import sys  # noqa: F401
from dataclasses import dataclass
from pathlib import Path

MAX_OUTPUT = 5_000


@dataclass
class RunResult:
    stdout: str
    stderr: str
    exit_code: int | None
    timed_out: bool

    @property
    def ok(self) -> bool:
        return self.exit_code == 0 and not self.timed_out


def _limit_memory(memory_mb: int):
    """Returns a preexec_fn. TODO: use resource.setrlimit(resource.RLIMIT_AS, (bytes, bytes)).
    Only on Linux (sys.platform == "linux"); on other systems return None."""
    raise NotImplementedError


def run_code(code: str, workdir: Path, timeout_s: float = 5, memory_mb: int = 1024) -> RunResult:
    # TODO: write code to workdir/"main.py"
    #       subprocess.run([sys.executable, "-I", "main.py"], cwd=workdir,
    #                      env={"PATH": os.environ.get("PATH", "")}, capture_output=True, text=True,
    #                      timeout=timeout_s, preexec_fn=_limit_memory(memory_mb))
    #       on subprocess.TimeoutExpired: RunResult("", "timed out", None, True)
    #       cut stdout and stderr to MAX_OUTPUT
    raise NotImplementedError
