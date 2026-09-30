import pytest

from track2_core.c4_evals.calibrate import agreement, cohens_kappa


def test_agreement():
    assert agreement(["pass", "fail", "pass", "fail"], ["pass", "pass", "pass", "fail"]) == 0.75


def test_kappa_perfect():
    assert cohens_kappa(["pass", "fail"], ["pass", "fail"]) == pytest.approx(1.0)


def test_kappa_known_value():
    human = ["pass"] * 5 + ["fail"] * 5
    judge = ["pass"] * 4 + ["fail"] + ["pass"] + ["fail"] * 4
    # p_o = 0.8, p_e = 0.5*0.5 + 0.5*0.5 = 0.5  ->  kappa = 0.6
    assert cohens_kappa(human, judge) == pytest.approx(0.6)


# TODO: a test for the judge with a fake llm that returns fixed JSON
# TODO: what should kappa be if the judge always says "pass"? Write the test, then check the math.
