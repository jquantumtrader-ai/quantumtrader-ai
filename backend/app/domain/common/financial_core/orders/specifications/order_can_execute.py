from __future__ import annotations

from dataclasses import dataclass

from ..entities.order import Order
from ..enums.order_status import OrderStatus


@dataclass(
    frozen=True
)
class OrderCanExecuteSpecification:
    """
    Regra que define se uma ordem
    pode ser executada.
    """


    def is_satisfied_by(
        self,
        order: Order,
    ) -> bool:

        return (
            order.status
            in (
                OrderStatus.CREATED,
                OrderStatus.PARTIALLY_FILLED,
            )
        )
