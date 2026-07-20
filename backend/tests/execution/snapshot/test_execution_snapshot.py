from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.snapshot import (
    ExecutionSnapshot,
)


def test_create_snapshot() -> None:

    execution_id = uuid4()

    snapshot = ExecutionSnapshot(
        execution_id=execution_id,
        quantity=Decimal("100"),
        filled_quantity=Decimal("35"),
        cancelled=False,
        created_at=datetime.utcnow(),
    )

    assert snapshot.execution_id == execution_id
    assert snapshot.quantity == Decimal("100")
    assert snapshot.filled_quantity == Decimal("35")
    assert snapshot.cancelled is False


def test_snapshot_is_frozen() -> None:

    snapshot = ExecutionSnapshot(
        execution_id=uuid4(),
        quantity=Decimal("100"),
        filled_quantity=Decimal("0"),
        cancelled=False,
        created_at=datetime.utcnow(),
    )

    with pytest.raises(
        FrozenInstanceError,
    ):

        snapshot.quantity = Decimal("50")
