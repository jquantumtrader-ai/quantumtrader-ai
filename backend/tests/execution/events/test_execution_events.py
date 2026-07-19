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
    )

    assert event.execution_id == execution_id

    assert event.event_type == (
        "EXECUTION_CREATED"
    )



def test_execution_filled_event():

    event = ExecutionFilledEvent(
        execution_id=uuid4(),
        quantity=Decimal(
            "100",
        ),
    )

    assert event.event_type == (
        "EXECUTION_FILLED"
    )

    assert event.payload[
        "quantity"
    ] == Decimal(
        "100",
    )



def test_execution_cancelled_event():

    event = ExecutionCancelledEvent(
        execution_id=uuid4(),
        reason="Broker rejected",
    )

    assert event.event_type == (
        "EXECUTION_CANCELLED"
    )

    assert event.payload[
        "reason"
    ] == "Broker rejected"
