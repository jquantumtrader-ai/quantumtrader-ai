from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..decimal_config import to_decimal
from ..exceptions import (
    InvalidOperationException,
)
from .base import ValueObject


@dataclass(
    frozen=True,
    slots=True
)
class NumericValue(ValueObject):
    """
    Objeto base para valores numéricos financeiros.

    Regras:

    - Usa Decimal internamente
    - Não aceita float
    - É imutável
    """

    value: Decimal


    def __init__(self, value):

        object.__setattr__(
            self,
            "value",
            to_decimal(value)
        )


    def __add__(
        self,
        other: NumericValue
    ) -> NumericValue:

        return NumericValue(
            self.value + other.value
        )


    def __sub__(
        self,
        other: NumericValue
    ) -> NumericValue:

        return NumericValue(
            self.value - other.value
        )


    def __mul__(
        self,
        other: NumericValue
    ) -> NumericValue:

        return NumericValue(
            self.value * other.value
        )


    def __truediv__(
        self,
        other: NumericValue
    ) -> NumericValue:

        if other.value == 0:

            raise InvalidOperationException(
                "Divisão por zero não permitida"
            )

        return NumericValue(
            self.value / other.value
        )


    def __eq__(
        self,
        other: object
    ) -> bool:

        if not isinstance(
            other,
            NumericValue
        ):
            return False

        return self.value == other.value


    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"({self.value})"
        )
