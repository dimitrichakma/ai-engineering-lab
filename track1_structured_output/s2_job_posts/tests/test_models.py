import pytest
from pydantic import ValidationError

from track1_structured_output.s2_job_posts.models import Salary


def test_salary_min_not_above_max():
    with pytest.raises(ValidationError):
        Salary(min_bdt=60000, max_bdt=45000, period="month")


def test_salary_can_be_partly_unknown():
    s = Salary(min_bdt=None, max_bdt=50000, period="month")
    assert s.max_bdt == 50000


# TODO: test that JobPost accepts salary=None.
# TODO: test that work_mode="wfh" is rejected.
# TODO: test to_row() flattens a JobPost with two requirements correctly.
