from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Sequence

from ...value_objects.money import Money


@dataclass(frozen=True)
class AllocationRequest:
    """
    Dados necessários para executar uma alocação.
    """

    amount: Money
    targets: Sequence[object]
    weights: Sequence[Decimal] | None = None


    def __post_init__(self) -> None:
        """
        Valida regras de negócio da solicitação.
        """

        if not self.targets:
            raise ValueError(
                "É necessário informar pelo menos um target."
            )


        if self.weights is not None:

            if len(self.weights) != len(self.targets):
                raise ValueError(
                    "Quantidade de pesos deve "
                    "ser igual aos targets."
                )


            for weight in self.weights:

                if weight < Decimal("0"):
                    raise ValueError(
                        "Peso não pode ser negativo."
                    )


                if weight > Decimal("100"):
                    raise ValueError(
                        "Peso não pode ser maior que 100."
                    )
