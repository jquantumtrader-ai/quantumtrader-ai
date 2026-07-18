from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..entities.order import Order
from ...value_objects.money import Money


@dataclass(frozen=True)
class OrderExecutionReport:
    """
    Relatório consolidado da execução
    de uma ordem.
    """

    order_id: str

    asset_symbol: str

    requested_quantity: Decimal

    executed_quantity: Decimal

    remaining_quantity: Decimal

    fills_count: int

    average_execution_price: Money | None

    executed_value: Money | None



    @classmethod
    def from_order(
        cls,
        order: Order,
    ) -> OrderExecutionReport:
        """
        Gera relatório a partir da ordem.
        """

        executed_value = None


        if order.average_execution_price:

            executed_value = Money(
                order.executed_quantity
                *
                order.average_execution_price.value,
                order.price.currency,
            )


        return cls(
            order_id=str(
                order.order_id.value
            ),

            asset_symbol=(
                order.asset.symbol
            ),

            requested_quantity=(
                order.quantity
            ),

            executed_quantity=(
                order.executed_quantity
            ),

            remaining_quantity=(
                order.remaining_quantity
            ),

            fills_count=len(
                order.fills
            ),

            average_execution_price=(
                order.average_execution_price
            ),

            executed_value=(
                executed_value
            ),
        )
