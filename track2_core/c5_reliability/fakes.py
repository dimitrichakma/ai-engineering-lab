"""Given. Fake models and error types. Do not change."""


class RetryableError(Exception):
    """Base for errors worth retrying."""


class ModelTimeout(RetryableError):
    pass


class RateLimited(RetryableError):
    pass


class ServerError(RetryableError):
    pass


class BadRequestError(Exception):
    """Not retryable: sending the same request again will fail again."""


class FlakyModel:
    """Plays back a script. Each item is an Exception instance (raised) or a str (returned).
    After the script ends, it repeats the LAST item forever."""

    def __init__(self, name: str, script: list):
        self.name = name
        self.script = list(script)
        self.calls = 0

    def generate(self, prompt: str) -> str:
        item = self.script[min(self.calls, len(self.script) - 1)]
        self.calls += 1
        if isinstance(item, Exception):
            raise item
        return f"{item}"
