from __future__ import annotations

from dataclasses import dataclass, field

from ..entities.order import Order
from ..order_id import OrderId


@dataclass
class MemoryOrderRepository:
    """
    Implementação em memória.

    Usada para testes e desenvolvimento.
    """


    _orders: dict[OrderId, Order] = field(
        default_factory=dict,
    )


    def save(
        self,
        order: Order,
    ) -> None:

        self._orders[
            order.order_id
        ] = order



    def get(
        self,
        order_id: OrderId,
    ) -> Order:

        if order_id not in self._orders:

            raise ValueError(
                "Ordem não encontrada."
            )


        return self._orders[
            order_id
        ]



    def exists(
        self,
        order_id: OrderId,
    ) -> bool:

        return (
            order_id
            in
            self._orders
        )



    def delete(
        self,
        order_id: OrderId,
    ) -> None:

        if order_id in self._orders:

            del self._orders[
                order_id
            ]



    def all(
        self,
    ) -> tuple[Order, ...]:

        return tuple(
            self._orders.values()
        )
