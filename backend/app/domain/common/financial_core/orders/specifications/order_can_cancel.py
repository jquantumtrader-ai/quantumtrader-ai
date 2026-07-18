from __future__ import annotations

from dataclasses import dataclass

from ..entities.order import Order
from ..enums.order_status import OrderStatus


@dataclass(
    frozen=True
)
class OrderCanCancelSpecification:
    """
    Regra que define se uma ordem
    pode ser cancelada.
    """


    def is_satisfied_by(
        self,
        order: Order,
    ) -> bool:

        return (
            order.status
            not in (
                OrderStatus.FILLED,
                OrderStatus.CANCELLED,
                OrderStatus.REJECTED,
            )
        )
