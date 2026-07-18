from __future__ import annotations

from dataclasses import dataclass, field

from ..entities.order import Order
from ..events import (
    OrderEvent,
    OrderCreated,
    OrderFilled,
    OrderCancelled,
    OrderRejected,
)



@dataclass
class OrderAggregate:
    """
    Aggregate Root da ordem.

    Controla estado e eventos
    produzidos pela ordem.
    """


    order: Order


    _events: list[OrderEvent] = field(
        default_factory=list
    )



    def record_event(
        self,
        event: OrderEvent,
    ) -> None:
        """
        Registra evento pendente.
        """

        self._events.append(
            event
        )



    def pull_events(
        self,
    ) -> tuple[OrderEvent, ...]:
        """
        Retorna eventos pendentes
        e limpa a fila.
        """

        events = tuple(
            self._events
        )


        self._events.clear()


        return events



    def created(
        self,
    ) -> None:
        """
        Registra criação da ordem.
        """

        self.record_event(
            OrderCreated(
                self.order.order_id
            )
        )



    def filled(
        self,
    ) -> None:
        """
        Registra execução.
        """

        self.record_event(
            OrderFilled(
                self.order.order_id
            )
        )



    def cancelled(
        self,
    ) -> None:
        """
        Registra cancelamento.
        """

        self.record_event(
            OrderCancelled(
                self.order.order_id
            )
        )



    def rejected(
        self,
    ) -> None:
        """
        Registra rejeição.
        """

        self.record_event(
            OrderRejected(
                self.order.order_id
            )
        )
