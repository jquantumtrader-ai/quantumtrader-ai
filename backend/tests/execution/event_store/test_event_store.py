from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.event_store import (
    InMemoryEventStore,
)

from app.domain.common.financial_core.execution.events import (
    ExecutionCreatedEvent,
)


def test_append_event():

    store = InMemoryEventStore()

    execution_id = uuid4()

    event = ExecutionCreatedEvent(
        execution_id=execution_id,
        quantity=Decimal("100"),
    )

    store.append(event)

    events = store.load(
        execution_id,
    )

    assert len(events) == 1
    assert events[0] == event


def test_empty_store():

    store = InMemoryEventStore()

    assert store.load(uuid4()) == []
