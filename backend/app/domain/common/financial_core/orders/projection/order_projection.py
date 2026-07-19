from __future__ import annotations

from dataclasses import dataclass

from ..entities.order import Order
from ..queries import OrderQueryModel
from ..read_store import OrderReadStore


@dataclass(slots=True)
class OrderProjection:
    """
    Projection responsável por transformar
    o Aggregate em um Read Model.

    Nesta primeira versão a projeção é
    sincronizada e atualiza diretamente
    o Read Store.
    """

    read_store: OrderReadStore

    def project(
        self,
        order: Order,
    ) -> OrderQueryModel:
        """
        Projeta uma Order para um
        OrderQueryModel.
        """

        query = OrderQueryModel.from_order(
            order,
        )

        self.read_store.write(
            query,
        )

        return query

    def remove(
        self,
        order_id: str,
    ) -> None:
        """
        Remove a projeção.
        """

        self.read_store.delete(
            order_id,
        )
