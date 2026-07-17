from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..assets.asset import Asset
from ...value_objects.money import Money


@dataclass(frozen=True)
class Position:
    """
    Representa uma posição financeira.

    Uma posição é composta por:

    - Ativo
    - Quantidade
    - Preço médio
    """

    asset: Asset
    quantity: Decimal
    average_price: Money


    def __post_init__(self) -> None:
        """
        Valida os dados da posição.
        """

        if self.quantity <= Decimal("0"):
            raise ValueError(
                "Quantidade deve ser maior que zero."
            )


    @property
    def cost_basis(self) -> Money:
        """
        Retorna o custo total da posição.
        """

        return Money(
            self.quantity * self.average_price.value,
            self.average_price.currency,
        )


    def market_value(
        self,
        current_price: Money,
    ) -> Money:
        """
        Calcula o valor de mercado atual.
        """

        if (
            current_price.currency
            != self.average_price.currency
        ):
            raise ValueError(
                "Moeda incompatível."
            )

        return Money(
            self.quantity
            * current_price.value,
            current_price.currency,
        )
