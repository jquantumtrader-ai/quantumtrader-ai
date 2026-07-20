from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.event_store import (
    InMemoryEventStore,
)

from app.domain.common.financial_core.execution.publishers import (
    ExecutionEventPublisher,
)

from app.domain.common.financial_core.execution.events import (
    ExecutionCreatedEvent,
)


def test_publish_event():

    store = InMemoryEventStore()

    publisher = ExecutionEventPublisher(
        store,
    )

    execution_id = uuid4()

    event = ExecutionCreatedEvent(
        execution_id,
        Decimal("100"),
    )

    publisher.publish(event)

    events = store.load(
        execution_id,
    )

    assert len(events) == 1
    assert events[0] == event


def test_publish_multiple_events():

    store = InMemoryEventStore()

    publisher = ExecutionEventPublisher(
        store,
    )

    execution_id = uuid4()

    publisher.publish(
        ExecutionCreatedEvent(
            execution_id,
            Decimal("100"),
        ),
    )

    publisher.publish(
        ExecutionCreatedEvent(
            execution_id,
            Decimal("100"),
        ),
    )

    assert len(store.load(execution_id)) == 2
