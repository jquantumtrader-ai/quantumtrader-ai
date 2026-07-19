from uuid import uuid4


from app.domain.common.financial_core.execution.event_store import (
    InMemoryEventStore,
)

from app.domain.common.financial_core.execution.events import (
    ExecutionCreatedEvent,
)

from app.domain.common.financial_core.execution.publishers import (
    ExecutionEventPublisher,
)



def test_publish_event():

    store = InMemoryEventStore()


    publisher = ExecutionEventPublisher(
        store,
    )


    execution_id = uuid4()


    event = ExecutionCreatedEvent(
        execution_id,
    )


    publisher.publish(
        [
            event,
        ],
    )


    events = store.get_events(
        execution_id,
    )


    assert len(events) == 1

    assert events[0] == event



def test_publish_empty_events():

    store = InMemoryEventStore()


    publisher = ExecutionEventPublisher(
        store,
    )


    publisher.publish(
        [],
    )


    assert store.get_events(
        uuid4(),
    ) == []
