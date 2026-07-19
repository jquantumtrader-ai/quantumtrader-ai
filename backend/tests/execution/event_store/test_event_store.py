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
    )


    store.append(
        event,
    )


    events = store.get_events(
        execution_id,
    )


    assert len(events) == 1

    assert events[0] == event



def test_empty_events():

    store = InMemoryEventStore()


    events = store.get_events(
        uuid4(),
    )


    assert events == []
