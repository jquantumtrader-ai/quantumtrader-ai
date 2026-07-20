from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)
from app.domain.common.financial_core.execution.snapshot import (
    ExecutionSnapshot,
    InMemorySnapshotRepository,
)


def test_save_and_load_snapshot() -> None:

    repository = InMemorySnapshotRepository()

    snapshot = ExecutionSnapshot(
        execution_id=uuid4(),
        quantity=Decimal("100"),
        filled_quantity=Decimal("40"),
        status=ExecutionStatus.PARTIAL,
        created_at=datetime.utcnow(),
    )

    repository.save(
        snapshot,
    )

    loaded = repository.load(
        snapshot.execution_id,
    )

    assert loaded == snapshot


def test_load_unknown_snapshot() -> None:

    repository = InMemorySnapshotRepository()

    loaded = repository.load(
        uuid4(),
    )

    assert loaded is None
