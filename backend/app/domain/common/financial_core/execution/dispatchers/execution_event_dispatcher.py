from __future__ import annotations

from collections import defaultdict
from typing import Callable

from ..events import ExecutionEvent


EventHandler = Callable[
    [ExecutionEvent],
    None,
]


class ExecutionEventDispatcher:
    """
    Dispatcher responsável por distribuir
    eventos de execução para handlers.
    """

    def __init__(self) -> None:

        self._handlers: dict[
            str,
            list[EventHandler],
        ] = defaultdict(list)


    def register(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        """
        Registra um handler para um tipo
        de evento.
        """

        self._handlers[
            event_type
        ].append(
            handler,
        )


    def dispatch(
        self,
        event: ExecutionEvent,
    ) -> None:
        """
        Publica um evento para todos
        os handlers registrados.
        """

        handlers = self._handlers.get(
            event.event_type,
            [],
        )

        for handler in handlers:
            handler(
                event,
            )


    def clear(
        self,
    ) -> None:
        """
        Remove todos os handlers.
        """

        self._handlers.clear()
