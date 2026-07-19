from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from ..orders import OrderId
from ..portfolio.assets.asset import Asset
from ..value_objects.money import Money


@dataclass(frozen=True, slots=True)
class Execution:
    """
    Representa uma execução de ordem.

    Uma Execution registra a execução
    efetiva de uma ordem no mercado.
    """

    execution_id: UUID

    order_id: OrderId

    asset: Asset

    quantity: Decimal

    price: Money

    executed_at: datetime

    @classmethod
    def create(
        cls,
        execution_id: UUID,
        order_id: OrderId,
        asset: Asset,
        quantity: Decimal,
        price: Money,
    ) -> "Execution":
        """
        Cria uma nova execução.
        """

        return cls(
            execution_id=execution_id,
            order_id=order_id,
            asset=asset,
            quantity=quantity,
            price=price,
            executed_at=datetime.utcnow(),
        )
