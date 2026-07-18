from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..entities.order import Order
from ..enums.order_status import OrderStatus


@dataclass(
    frozen=True
)
class OrderCompletedSpecification:
    """
    Regra que define se uma ordem
    está concluída.
    """


    def is_satisfied_by(
        self,
        order: Order,
    ) -> bool:

        if (
            order.status
            ==
            OrderStatus.FILLED
        ):
            return True


        filled = sum(
            fill.quantity
            for fill in order.fills
        )


        return (
            order.quantity - filled
            ==
            Decimal("0")
        )
