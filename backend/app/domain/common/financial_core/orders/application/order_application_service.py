from __future__ import annotations

from dataclasses import dataclass

from ..aggregate import OrderAggregate
from ..commands import (
    CancelOrderCommand,
    CreateOrderCommand,
    FillOrderCommand,
    RejectOrderCommand,
)
from ..handlers import OrderCommandHandler


@dataclass
class OrderApplicationService:
    """
    Camada de aplicação responsável por
    orquestrar operações relacionadas
    às ordens.
    """

    handler: OrderCommandHandler = OrderCommandHandler()

    def create_order(
        self,
        command: CreateOrderCommand,
    ) -> OrderAggregate:
        """
        Cria uma nova ordem.
        """

        return self.handler.handle_create(
            command,
        )

    def cancel_order(
        self,
        aggregate: OrderAggregate,
        command: CancelOrderCommand,
    ) -> None:
        """
        Cancela uma ordem.
        """

        self.handler.handle_cancel(
            aggregate,
            command,
        )

    def fill_order(
        self,
        aggregate: OrderAggregate,
        command: FillOrderCommand,
    ) -> None:
        """
        Marca uma ordem como executada.
        """

        self.handler.handle_fill(
            aggregate,
            command,
        )

    def reject_order(
        self,
        aggregate: OrderAggregate,
        command: RejectOrderCommand,
    ) -> None:
        """
        Rejeita uma ordem.
        """

        self.handler.handle_reject(
            aggregate,
            command,
        )
