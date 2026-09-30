import pytest

from track6_models.m2_embeddings.compare_embeddings import cosine, hit_at_k, mrr, rank


def test_cosine():
    assert cosine([1, 0], [1, 0]) == pytest.approx(1.0)
    assert cosine([1, 0], [0, 1]) == pytest.approx(0.0)


def test_rank():
    assert rank([1, 0], [[0, 1], [1, 0], [0.7, 0.7]]) == [1, 2, 0]


def test_hit_at_k():
    assert not hit_at_k([False, False, True], 2)
    assert hit_at_k([False, False, True], 3)


def test_mrr():
    assert mrr([[True, False], [False, True], [False, False]]) == pytest.approx((1 + 0.5 + 0) / 3)
