from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from .execution_snapshot import ExecutionSnapshot


class SnapshotRepository(ABC):
    """
    Contrato para armazenamento de snapshots.
    """

    @abstractmethod
    def save(
        self,
        snapshot: ExecutionSnapshot,
    ) -> None:
        """
        Persiste um snapshot.
        """

    @abstractmethod
    def load(
        self,
        execution_id: UUID,
    ) -> ExecutionSnapshot | None:
        """
        Recupera o snapshot mais recente.
        """
