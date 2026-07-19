from __future__ import annotations

from ..event_store import EventStore
from ..events import ExecutionEvent



class ExecutionEventPublisher:
    """
    Publicador responsável por enviar
    eventos de domínio para o Event Store.
    """


    def __init__(
        self,
        event_store: EventStore,
    ) -> None:

        self._event_store = event_store



    def publish(
        self,
        events: list[ExecutionEvent],
    ) -> None:
        """
        Publica uma lista de eventos.
        """


        for event in events:

            self._event_store.append(
                event,
            )
