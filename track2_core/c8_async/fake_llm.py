"""Given. An async fake model. Do not change."""
import asyncio


class FakeAsyncLLM:
    def __init__(self, delay: float = 0.1, fail_every: int = 0):
        self.delay = delay
        self.fail_every = fail_every      # 0 = never fail; 5 = every 5th call fails
        self.calls = 0
        self.running = 0
        self.max_running = 0

    async def classify(self, text: str) -> str:
        self.calls += 1
        n = self.calls
        self.running += 1
        self.max_running = max(self.max_running, self.running)
        try:
            await asyncio.sleep(self.delay)
            if self.fail_every and n % self.fail_every == 0:
                raise RuntimeError(f"fake failure on call {n}")
            return "positive" if "good" in text.lower() else "neutral"
        finally:
            self.running -= 1
