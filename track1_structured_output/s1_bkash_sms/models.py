from typing import Literal

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    provider: Literal["bkash", "nagad","unknown"] = Field(description="The provider of transaction")
    kind: Literal["send_money", "cash_in", "cash_out", "payment", "received", "other"] = Field(description="The method of transaction. Cash_in means adding money to the account, cash_out means withdrawing money from the account, payment means paying to a merchant, send_money means sending money to another person, received means receiving money from another person, other means any other type of transaction")
    amount_bdt: float = Field(gt=0, description="The amount of transaction in bdt as written in the sms")
    fee_bdt: float | None = Field(default=None, description="The fee of transaction in bdt")
    counterparty: str | None = Field(default=None, description="Cash_in: the source of money, Cash_out: the destination of money, send_money: the recipient of money, received: the sender of money, payment: the merchant name, other: any other relevant information")
    balance_bdt: float | None = Field(default=None, description="The balance after transaction")
    trx_id: str | None = Field(default=None, description="The transaction id")
    date_text: str | None = Field(default=None, description="The date of transaction in text format")


