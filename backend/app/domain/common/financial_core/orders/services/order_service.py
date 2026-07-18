from __future__ import annotations

from dataclasses import dataclass

from ..entities.order import Order
from ..order_id import OrderId
from ..repository.order_repository import OrderRepository



@dataclass
class OrderService:
    """
    Serviço de aplicação responsável
    pelo ciclo operacional das ordens.
    """


    repository: OrderRepository



    def create(
        self,
        order: Order,
    ) -> Order:
        """
        Registra uma nova ordem.
        """

        if self.repository.exists(
            order.order_id
        ):

            raise ValueError(
                "Ordem já existente."
            )


        self.repository.save(
            order
        )

        return order



    def get(
        self,
        order_id: OrderId,
    ) -> Order:
        """
        Busca uma ordem.
        """

        return self.repository.get(
            order_id
        )



    def cancel(
        self,
        order_id: OrderId,
    ) -> Order:
        """
        Cancela uma ordem existente.
        """

        order = self.repository.get(
            order_id
        )


        cancelled = (
            order.cancel()
        )


        self.repository.save(
            cancelled
        )


        return cancelled



    def list_orders(
        self,
    ) -> tuple[Order, ...]:
        """
        Lista todas as ordens.
        """

        return self.repository.all()



    def update(
        self,
        order: Order,
    ) -> None:
        """
        Atualiza uma ordem.
        """

        self.repository.save(
            order
        )
