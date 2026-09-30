from track2_core.c9_caching.cache import ExactCache, SemanticCache, cache_key, cached_generate


class FakeClock:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t


def test_key_depends_on_model_and_settings():
    a = cache_key("m1", "hi", {"temperature": 0})
    assert a == cache_key("m1", "hi", {"temperature": 0})
    assert a != cache_key("m2", "hi", {"temperature": 0})
    assert a != cache_key("m1", "hi", {"temperature": 1})


def test_exact_cache_ttl():
    clock = FakeClock()
    c = ExactCache(ttl_seconds=60, clock=clock)
    c.set("k", "answer")
    assert c.get("k") == "answer"
    clock.t += 61
    assert c.get("k") is None


def fake_embed(texts):
    # two "topics": texts with "bus" point one way, others the other way
    return [[1.0, 0.0] if "bus" in t.lower() else [0.0, 1.0] for t in texts]


def test_semantic_hit_and_miss():
    s = SemanticCache(fake_embed, threshold=0.9)
    s.set("bus refund?", "Bus answer")
    hit = s.get("refund for my BUS ticket")
    assert hit is not None and hit[0] == "Bus answer"
    assert s.get("train refund?") is None


def test_cached_generate_calls_model_once():
    calls = []

    def llm(p):
        calls.append(p)
        return "fresh"

    exact = ExactCache()
    assert cached_generate("q", llm, exact, None) == ("fresh", "model")
    assert cached_generate("q", llm, exact, None) == ("fresh", "exact")
    assert len(calls) == 1

# TODO: semantic source is returned when exact misses but semantic hits
