from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Type

from ..order_event import OrderEvent



EventHandler = Callable[
    [OrderEvent],
    None,
]



@dataclass
class OrderEventDispatcher:
    """
    Dispatcher responsável por publicar
    eventos de domínio de ordens.
    """


    _handlers: dict[
        Type[OrderEvent],
        list[EventHandler],
    ] = field(
        default_factory=lambda:
        defaultdict(list)
    )



    def register(
        self,
        event_type: Type[OrderEvent],
        handler: EventHandler,
    ) -> None:
        """
        Registra um handler para um evento.
        """

        self._handlers[
            event_type
        ].append(
            handler
        )



    def dispatch(
        self,
        event: OrderEvent,
    ) -> None:
        """
        Publica um evento.
        """

        handlers = self._handlers.get(
            type(event),
            [],
        )


        for handler in handlers:

            handler(
                event
            )



    def clear(
        self,
    ) -> None:
        """
        Remove todos handlers.
        """

        self._handlers.clear()
