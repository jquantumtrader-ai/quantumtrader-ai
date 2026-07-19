from __future__ import annotations

from dataclasses import dataclass

from ..entities.order import Order
from ..queries import OrderQueryModel


@dataclass(slots=True)
class OrderQueryService:
    """
    Serviço responsável por fornecer modelos
    de consulta (CQRS Read Model) para Ordens.
    """

    def get(
        self,
        order: Order,
    ) -> OrderQueryModel:
        """
        Retorna um Query Model para uma ordem.
        """

        return OrderQueryModel.from_order(
            order,
        )

    def get_many(
        self,
        orders: list[Order],
    ) -> list[OrderQueryModel]:
        """
        Retorna uma lista de Query Models.
        """

        return [
            OrderQueryModel.from_order(
                order,
            )
            for order in orders
        ]
