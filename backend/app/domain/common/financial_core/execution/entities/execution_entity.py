from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from ...orders import OrderId
from ...portfolio.assets.asset import Asset
from ...value_objects.money import Money


class ExecutionEntity:
    """
    Entidade de domínio responsável por representar
    uma execução real de uma ordem.
    """

    def __init__(
        self,
        execution_id: UUID,
        order_id: OrderId,
        asset: Asset,
        quantity: Decimal,
        price: Money,
        executed_at: datetime,
    ) -> None:

        self._validate_quantity(
            quantity,
        )

        self.execution_id = execution_id
        self.order_id = order_id
        self.asset = asset
        self.quantity = quantity
        self.price = price
        self.executed_at = executed_at

    @staticmethod
    def _validate_quantity(
        quantity: Decimal,
    ) -> None:
        """
        Quantidade executada deve ser positiva.
        """

        if quantity <= Decimal("0"):
            raise ValueError(
                "Execution quantity must be positive"
            )

    def is_same_execution(
        self,
        other: "ExecutionEntity",
    ) -> bool:
        """
        Compara duas execuções pela identidade.
        """

        return (
            self.execution_id
            ==
            other.execution_id
        )

    @classmethod
    def create(
        cls,
        execution_id: UUID,
        order_id: OrderId,
        asset: Asset,
        quantity: Decimal,
        price: Money,
    ) -> "ExecutionEntity":
        """
        Factory de criação.
        """

        return cls(
            execution_id=execution_id,
            order_id=order_id,
            asset=asset,
            quantity=quantity,
            price=price,
            executed_at=datetime.utcnow(),
        )
