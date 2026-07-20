from __future__ import annotations

from uuid import UUID

from .execution_snapshot import ExecutionSnapshot
from .snapshot_repository import SnapshotRepository


class InMemorySnapshotRepository(SnapshotRepository):
    """
    Implementação em memória do SnapshotRepository.
    """

    def __init__(
        self,
    ) -> None:

        self._snapshots: dict[
            UUID,
            ExecutionSnapshot,
        ] = {}

    def save(
        self,
        snapshot: ExecutionSnapshot,
    ) -> None:

        self._snapshots[
            snapshot.execution_id
        ] = snapshot

    def load(
        self,
        execution_id: UUID,
    ) -> ExecutionSnapshot | None:

        return self._snapshots.get(
            execution_id,
        )
