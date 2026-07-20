from __future__ import annotations

from datetime import datetime

from ..aggregates import ExecutionAggregate
from ..enums import ExecutionStatus
from .execution_snapshot import ExecutionSnapshot


class ExecutionSnapshotService:
    """
    Serviço responsável por criar e restaurar snapshots.
    """

    def create_snapshot(
        self,
        aggregate: ExecutionAggregate,
    ) -> ExecutionSnapshot:

        return ExecutionSnapshot(
            execution_id=aggregate.execution_id,
            quantity=aggregate.quantity,
            filled_quantity=aggregate.filled_quantity,
            status=aggregate.status,
            created_at=datetime.utcnow(),
        )

    def restore(
        self,
        snapshot: ExecutionSnapshot,
    ) -> ExecutionAggregate:

        aggregate = ExecutionAggregate(
            execution_id=snapshot.execution_id,
            quantity=snapshot.quantity,
        )

        aggregate.pull_events()

        if snapshot.filled_quantity > 0:

            aggregate.add_fill(
                snapshot.filled_quantity,
            )

            aggregate.pull_events()

        if snapshot.status == ExecutionStatus.CANCELLED:

            aggregate.cancel(
                "snapshot restore",
            )

            aggregate.pull_events()

        return aggregate
