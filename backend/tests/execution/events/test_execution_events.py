from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.events import (
    ExecutionCreatedEvent,
    ExecutionFilledEvent,
    ExecutionCancelledEvent,
)


def test_execution_created_event():

    execution_id = uuid4()

    event = ExecutionCreatedEvent(
        execution_id,
        Decimal("100"),
    )

    assert event.execution_id == execution_id
    assert event.event_type == "EXECUTION_CREATED"
    assert event.payload["quantity"] == Decimal("100")


def test_execution_filled_event():

    execution_id = uuid4()

    event = ExecutionFilledEvent(
        execution_id,
        Decimal("25"),
    )

    assert event.execution_id == execution_id
    assert event.payload["quantity"] == Decimal("25")


def test_execution_cancelled_event():

    execution_id = uuid4()

    event = ExecutionCancelledEvent(
        execution_id,
        "Rejected",
    )

    assert event.execution_id == execution_id
    assert event.payload["reason"] == "Rejected"
