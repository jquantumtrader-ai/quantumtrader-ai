from __future__ import annotations

from dataclasses import dataclass, field

from ..entities.order import Order
from ..order_id import OrderId


@dataclass
class OrderManager:
    """
    Gerenciador de ordens.

    Mantém controle das ordens
    criadas no domínio.
    """

    _orders: dict[OrderId, Order] = field(
        default_factory=dict,
    )


    def register(
        self,
        order: Order,
    ) -> None:
        """
        Registra uma ordem.
        """

        if order.order_id in self._orders:

            raise ValueError(
                "Ordem já registrada."
            )


        self._orders[
            order.order_id
        ] = order



    def get(
        self,
        order_id: OrderId,
    ) -> Order:
        """
        Busca uma ordem.
        """

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



    def all(
        self,
    ) -> tuple[Order, ...]:
        """
        Retorna todas as ordens.
        """

        return tuple(
            self._orders.values()
        )



    def cancel(
        self,
        order_id: OrderId,
    ) -> Order:
        """
        Cancela uma ordem.
        """

        order = self.get(
            order_id
        )


        cancelled = order.cancel()


        self._orders[
            order_id
        ] = cancelled


        return cancelled



    def update(
        self,
        order: Order,
    ) -> None:
        """
        Atualiza uma ordem existente.
        """

        if order.order_id not in self._orders:

            raise ValueError(
                "Ordem não registrada."
            )


        self._orders[
            order.order_id
        ] = order
