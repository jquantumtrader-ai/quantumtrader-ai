from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)
from app.domain.common.financial_core.execution.snapshot import (
    ExecutionSnapshot,
)


def test_snapshot_creation() -> None:

    snapshot = ExecutionSnapshot(
        execution_id=uuid4(),
        quantity=Decimal("100"),
        filled_quantity=Decimal("40"),
        status=ExecutionStatus.PARTIAL,
        created_at=datetime.utcnow(),
    )

    assert snapshot.quantity == Decimal("100")
    assert snapshot.filled_quantity == Decimal("40")
    assert snapshot.status == ExecutionStatus.PARTIAL


def test_snapshot_is_frozen() -> None:

    snapshot = ExecutionSnapshot(
        execution_id=uuid4(),
        quantity=Decimal("10"),
        filled_quantity=Decimal("0"),
        status=ExecutionStatus.CREATED,
        created_at=datetime.utcnow(),
    )

    with pytest.raises(Exception):
        snapshot.quantity = Decimal("20")
