from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from ..decimal_config import to_decimal
from .base import ValueObject


@dataclass(
    frozen=True,
    slots=True,
)
class NumericValue(ValueObject):
    """
    Classe base para todos os Value Objects numéricos.

    Responsabilidades:

    - Armazenar um Decimal
    - Garantir imutabilidade
    - Padronizar igualdade
    - Padronizar representação

    Não implementa operações matemáticas.
    """

    value: Decimal

    def __init__(self, value: Any) -> None:
        object.__setattr__(
            self,
            "value",
            to_decimal(value),
        )

    def as_decimal(self) -> Decimal:
        """
        Retorna o Decimal interno.
        """
        return self.value

    def __eq__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, NumericValue):
            return False

        return self.value == other.value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(value={self.value})"
        )
