from __future__ import annotations

from ..currency.currency import Currency
from .financial import FinancialValue


class Money(FinancialValue):
    """
    Representa um valor monetário associado a uma moeda.
    """

    currency: Currency

    def __init__(self, value, currency: Currency) -> None:
        super().__init__(value)
        object.__setattr__(self, "currency", currency)

    def __str__(self) -> str:
        return f"{self.currency.code} {self.as_string()}"

    def __repr__(self) -> str:
        return (
            f"Money(value={self.as_string()}, "
            f"currency='{self.currency.code}')"
        )
