from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..entities.order import Order


@dataclass(frozen=True)
class OrderQueryModel:
    """
    Modelo de leitura (CQRS) para Ordens.

    Expõe somente dados para consulta,
    sem qualquer comportamento de domínio.
    """

    order_id: str

    asset: str

    side: str

    order_type: str

    status: str

    quantity: Decimal

    price: Decimal

    fills: int

    @classmethod
    def from_order(
        cls,
        order: Order,
    ) -> "OrderQueryModel":
        """
        Constrói um modelo de consulta
        a partir de uma entidade Order.
        """

        return cls(
            order_id=str(
                order.order_id.value,
            ),
            asset=order.asset.symbol,
            side=order.side.value,
            order_type=order.order_type.value,
            status=order.status.value,
            quantity=order.quantity,
            price=order.price.value,
            fills=len(
                order.fills,
            ),
        )
