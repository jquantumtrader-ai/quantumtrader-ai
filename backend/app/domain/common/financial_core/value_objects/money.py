from __future__ import annotations

from typing import Any

from ..currency.currency import Currency
from .financial import FinancialValue
from .money_exceptions import CurrencyMismatchError
from .numeric import NumericValue


class Money(FinancialValue):
    """
    Representa um valor monetário associado a uma moeda.
    """

    currency: Currency

    def __init__(
        self,
        value: Any,
        currency: Currency,
    ) -> None:

        super().__init__(value)

        object.__setattr__(
            self,
            "currency",
            currency,
        )

    def _validate_currency(
        self,
        other: Money,
    ) -> None:

        if self.currency != other.currency:
            raise CurrencyMismatchError(
                "Não é permitido operar moedas diferentes."
            )

    def __add__(
        self,
        other: NumericValue,
    ) -> Money:

        if not isinstance(other, Money):
            raise TypeError(
                "Money só pode operar com outro Money."
            )

        self._validate_currency(other)

        return Money(
            self.value + other.value,
            self.currency,
        )

    def __sub__(
        self,
        other: NumericValue,
    ) -> Money:

        if not isinstance(other, Money):
            raise TypeError(
                "Money só pode operar com outro Money."
            )

        self._validate_currency(other)

        return Money(
            self.value - other.value,
            self.currency,
        )

    def __lt__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, Money):
            return NotImplemented

        self._validate_currency(other)

        return self.value < other.value

    def __le__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, Money):
            return NotImplemented

        self._validate_currency(other)

        return self.value <= other.value

    def __gt__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, Money):
            return NotImplemented

        self._validate_currency(other)

        return self.value > other.value

    def __ge__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, Money):
            return NotImplemented

        self._validate_currency(other)

        return self.value >= other.value

    def max(
        self,
        other: Money,
    ) -> Money:

        self._validate_currency(other)

        return self if self >= other else other

    def min(
        self,
        other: Money,
    ) -> Money:

        self._validate_currency(other)

        return self if self <= other else other

    def __str__(self) -> str:

        return (
            f"{self.currency.code} "
            f"{self.as_string()}"
        )

    def __repr__(self) -> str:

        return (
            f"Money("
            f"value={self.as_string()}, "
            f"currency='{self.currency.code}'"
            f")"
        )
