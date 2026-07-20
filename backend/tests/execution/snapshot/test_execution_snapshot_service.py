from __future__ import annotations

from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.aggregates import (
    ExecutionAggregate,
)
from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)
from app.domain.common.financial_core.execution.snapshot import (
    ExecutionSnapshotService,
)


def test_create_snapshot() -> None:

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    aggregate.pull_events()

    aggregate.add_fill(
        Decimal("25"),
    )

    aggregate.pull_events()

    service = ExecutionSnapshotService()

    snapshot = service.create_snapshot(
        aggregate,
    )

    assert snapshot.execution_id == aggregate.execution_id
    assert snapshot.quantity == Decimal("100")
    assert snapshot.filled_quantity == Decimal("25")
    assert snapshot.status == ExecutionStatus.PARTIAL


def test_restore_snapshot() -> None:

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    aggregate.pull_events()

    aggregate.add_fill(
        Decimal("40"),
    )

    aggregate.pull_events()

    service = ExecutionSnapshotService()

    snapshot = service.create_snapshot(
        aggregate,
    )

    restored = service.restore(
        snapshot,
    )

    assert restored.execution_id == aggregate.execution_id
    assert restored.quantity == Decimal("100")
    assert restored.filled_quantity == Decimal("40")
    assert restored.status == ExecutionStatus.PARTIAL
