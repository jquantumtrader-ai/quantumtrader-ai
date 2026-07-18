from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4


from .. import OrderId

from ..aggregate import OrderAggregate

from ..commands import (
    CreateOrderCommand,
    CancelOrderCommand,
    FillOrderCommand,
    RejectOrderCommand,
)

from ..entities.order import Order

from ..enums import OrderStatus



@dataclass
class OrderCommandHandler:
    """
    Responsável por executar comandos
    relacionados ao agregado Order.
    """


    def handle_create(
        self,
        command: CreateOrderCommand,
    ) -> OrderAggregate:
        """
        Cria uma nova ordem.
        """


        order = Order(
            order_id=OrderId(
                uuid4(),
            ),
            asset=command.asset,
            side=command.side,
            order_type=command.order_type,
            status=OrderStatus.CREATED,
            quantity=command.quantity,
            price=command.price,
        )


        return OrderAggregate(
            order,
        )



    def handle_cancel(
        self,
        aggregate: OrderAggregate,
        command: CancelOrderCommand,
    ) -> None:
        """
        Cancela uma ordem.
        """

        aggregate.order.cancel()



    def handle_fill(
        self,
        aggregate: OrderAggregate,
        command: FillOrderCommand,
    ) -> None:
        """
        Preenche uma ordem.
        """

        aggregate.order.fill()



    def handle_reject(
        self,
        aggregate: OrderAggregate,
        command: RejectOrderCommand,
    ) -> None:
        """
        Rejeita uma ordem.
        """

        aggregate.order.reject()
