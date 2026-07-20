from __future__ import annotations

from uuid import UUID

from ..aggregates import ExecutionAggregate
from ..event_store import EventStore
from ..replay import ExecutionEventReplayService


class ExecutionAggregateLoader:
    """
    Responsável por reconstruir um ExecutionAggregate
    a partir dos eventos armazenados no Event Store.
    """

    def __init__(
        self,
        event_store: EventStore,
        replay_service: ExecutionEventReplayService,
    ) -> None:
        self._event_store = event_store
        self._replay_service = replay_service

    def load(
        self,
        execution_id: UUID,
    ) -> ExecutionAggregate:
        """
        Carrega um aggregate através do histórico
        de eventos persistidos.
        """

        events = self._event_store.get_events(
            execution_id,
        )

        if not events:
            raise ValueError(
                "Execution not found",
            )

        return self._replay_service.replay(
            events,
        )
