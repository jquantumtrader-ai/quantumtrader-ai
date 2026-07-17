from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ...value_objects.money import Money


@dataclass(frozen=True)
class AllocationResult:
    """
    Resultado final de uma alocação financeira.

    Representa:
    - ativo/destino
    - valor alocado
    - peso utilizado

    Mantém compatibilidade com versões antigas
    que acessavam Money diretamente.
    """

    target: object
    amount: Money
    weight: Decimal


    def __post_init__(self) -> None:
        """
        Valida invariantes do resultado.
        """

        if self.weight < Decimal("0"):
            raise ValueError(
                "Peso não pode ser negativo."
            )


        if self.weight > Decimal("100"):
            raise ValueError(
                "Peso não pode ser maior que 100."
            )


    @property
    def value(self) -> Decimal:
        """
        Compatibilidade com o contrato antigo.
        """

        return self.amount.value


    @property
    def currency(self):
        """
        Compatibilidade com o contrato antigo.
        """

        return self.amount.currency
