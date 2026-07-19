from __future__ import annotations

from collections import defaultdict
from uuid import UUID

from ..events import ExecutionEvent

from .event_store import EventStore



class InMemoryEventStore(EventStore):
    """
    Implementação em memória
    do Event Store.
    """


    def __init__(
        self,
    ) -> None:

        self._events: dict[
            UUID,
            list[ExecutionEvent],
        ] = defaultdict(list)



    def append(
        self,
        event: ExecutionEvent,
    ) -> None:
        """
        Adiciona evento ao armazenamento.
        """

        self._events[
            event.execution_id
        ].append(
            event,
        )



    def get_events(
        self,
        execution_id: UUID,
    ) -> list[ExecutionEvent]:
        """
        Busca eventos da execução.
        """

        return list(
            self._events.get(
                execution_id,
                [],
            )
        )
