"""Tests for the model only. They do not call the LLM, so they are fast and free."""
import pytest
from pydantic import ValidationError

from track1_structured_output.s1_bkash_sms.models import Transaction


def valid_data(**overrides):
    data = {
        "provider": "bkash",
        "kind": "send_money",
        "amount_bdt": 500.0,
        "fee_bdt": 5.0,
        "counterparty": "01822000002",
        "balance_bdt": 2745.5,
        "trx_id": "BKX11AA02",
        "date_text": "13/09/2026 09:10",
    }
    data.update(overrides)
    return data


def test_valid_transaction_parses():
    t = Transaction(**valid_data())
    assert t.amount_bdt == 500.0


def test_amount_must_be_positive():
    with pytest.raises(ValidationError):
        Transaction(**valid_data(amount_bdt=0))


# TODO: add a test that provider="bikash" (typo) is rejected.
# TODO: add a test that fee_bdt=None is allowed.
