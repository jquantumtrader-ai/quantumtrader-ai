from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ...value_objects.money import Money
from ..order_id import OrderId



@dataclass(
    frozen=True,
)
class Fill:
    """
    Representa uma execução individual
    de uma ordem.
    """


    order_id: OrderId

    quantity: Decimal

    price: Money



    def __post_init__(
        self,
    ) -> None:

        if self.quantity <= Decimal("0"):

            raise ValueError(
                "Quantidade executada deve ser maior que zero."
            )


    @property
    def value(
        self,
    ) -> Money:
        """
        Valor financeiro da execução.
        """

        return Money(
            self.quantity
            *
            self.price.value,
            self.price.currency,
        )
