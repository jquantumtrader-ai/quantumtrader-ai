from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

from ..entities.order import Order
from ..enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from ...portfolio.assets.asset import Asset
from ...value_objects.money import Money
from .. import OrderId


@dataclass(frozen=True, slots=True)
class OrderSnapshot:
    """
    Representa um snapshot imutável
    do estado de uma Order.

    Usado para recuperação,
    persistência e auditoria.
    """

    order_id: OrderId

    asset: Asset

    side: OrderSide

    order_type: OrderType

    status: OrderStatus

    quantity: Decimal

    price: Money

    created_at: datetime

    @classmethod
    def from_order(
        cls,
        order: Order,
    ) -> "OrderSnapshot":
        """
        Cria um snapshot a partir
        de uma Order atual.
        """

        return cls(
            order_id=order.order_id,
            asset=order.asset,
            side=order.side,
            order_type=order.order_type,
            status=order.status,
            quantity=order.quantity,
            price=order.price,
            created_at=datetime.utcnow(),
        )

    def restore(
        self,
    ) -> Order:
        """
        Restaura uma Order
        a partir do snapshot.
        """

        return Order(
            order_id=self.order_id,
            asset=self.asset,
            side=self.side,
            order_type=self.order_type,
            status=self.status,
            quantity=self.quantity,
            price=self.price,
        )
