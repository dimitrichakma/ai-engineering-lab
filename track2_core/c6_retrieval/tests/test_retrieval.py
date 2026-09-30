import pytest

from track2_core.c6_retrieval.chunkers import by_heading, fixed_size
from track2_core.c6_retrieval.search import VectorIndex, cosine, rrf


def test_fixed_size_overlap():
    words = " ".join(str(i) for i in range(10))
    chunks = fixed_size(words, size_words=4, overlap_words=2)
    assert chunks[0] == "0 1 2 3"
    assert chunks[1] == "2 3 4 5"


def test_fixed_size_rejects_bad_overlap():
    with pytest.raises(ValueError):
        fixed_size("a b c", size_words=2, overlap_words=2)


def test_by_heading_keeps_headings():
    text = "# Title\nintro\n## A\none\n## B\ntwo"
    assert by_heading(text) == ["## A\none", "## B\ntwo"]


def test_cosine():
    assert cosine([1, 0], [1, 0]) == pytest.approx(1.0)
    assert cosine([1, 0], [0, 1]) == pytest.approx(0.0)


def test_rrf_rewards_items_found_by_both():
    fused = rrf([["a", "b", "c"], ["c", "a", "d"]], k=2)
    assert fused[0] == "a"


# TODO: test VectorIndex with a FAKE embed function (e.g. map each text to [len(text), 1])
#       so no model is called
# TODO: test hit_at_k in experiment.py is case insensitive
