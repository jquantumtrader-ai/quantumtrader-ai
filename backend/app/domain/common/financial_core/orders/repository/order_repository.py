from __future__ import annotations

from typing import Protocol

from ..entities.order import Order
from ..order_id import OrderId


class OrderRepository(Protocol):
    """
    Contrato de persistência
    de ordens.
    """


    def save(
        self,
        order: Order,
    ) -> None:
        ...


    def get(
        self,
        order_id: OrderId,
    ) -> Order:
        ...


    def exists(
        self,
        order_id: OrderId,
    ) -> bool:
        ...


    def delete(
        self,
        order_id: OrderId,
    ) -> None:
        ...


    def all(
        self,
    ) -> tuple[Order, ...]:
        ...
