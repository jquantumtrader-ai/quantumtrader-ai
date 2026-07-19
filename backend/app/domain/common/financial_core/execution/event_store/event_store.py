from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from ..events import ExecutionEvent


class EventStore(ABC):
    """
    Contrato para armazenamento
    de eventos de domínio.
    """


    @abstractmethod
    def append(
        self,
        event: ExecutionEvent,
    ) -> None:
        """
        Persiste um evento.
        """

        raise NotImplementedError



    @abstractmethod
    def get_events(
        self,
        execution_id: UUID,
    ) -> list[ExecutionEvent]:
        """
        Retorna eventos de uma execução.
        """

        raise NotImplementedError
