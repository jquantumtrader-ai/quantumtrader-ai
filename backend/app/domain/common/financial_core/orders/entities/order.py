from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ...portfolio.assets.asset import Asset
from ...value_objects.money import Money
from ..order_id import OrderId


@dataclass(frozen=True)
class Order:
    """
    Representa uma ordem financeira.
    """

    order_id: OrderId

    asset: Asset

    quantity: Decimal

    price: Money

    def __post_init__(
        self,
    ) -> None:

        if self.quantity <= Decimal("0"):
            raise ValueError(
                "Quantidade deve ser maior que zero."
            )

    @property
    def notional(
        self,
    ) -> Money:
        """
        Valor financeiro da ordem.
        """

        return Money(
            self.quantity
            * self.price.value,
            self.price.currency,
        )
