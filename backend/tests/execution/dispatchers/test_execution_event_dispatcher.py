from uuid import uuid4

from app.domain.common.financial_core.execution.dispatchers import (
    ExecutionEventDispatcher,
)

from app.domain.common.financial_core.execution.events import (
    ExecutionCreatedEvent,
)



def test_register_and_dispatch_event():

    dispatcher = ExecutionEventDispatcher()

    received = []


    def handler(event):

        received.append(
            event,
        )


    dispatcher.register(
        "EXECUTION_CREATED",
        handler,
    )


    event = ExecutionCreatedEvent(
        uuid4(),
    )


    dispatcher.dispatch(
        event,
    )


    assert len(
        received,
    ) == 1


    assert received[0] == event



def test_multiple_handlers():

    dispatcher = ExecutionEventDispatcher()

    counter = {
        "value": 0,
    }


    def handler_one(event):

        counter["value"] += 1


    def handler_two(event):

        counter["value"] += 1


    dispatcher.register(
        "EXECUTION_CREATED",
        handler_one,
    )

    dispatcher.register(
        "EXECUTION_CREATED",
        handler_two,
    )


    dispatcher.dispatch(
        ExecutionCreatedEvent(
            uuid4(),
        ),
    )


    assert counter["value"] == 2



def test_clear_handlers():

    dispatcher = ExecutionEventDispatcher()

    called = []


    dispatcher.register(
        "EXECUTION_CREATED",
        lambda event: called.append(event),
    )


    dispatcher.clear()


    dispatcher.dispatch(
        ExecutionCreatedEvent(
            uuid4(),
        ),
    )


    assert called == []
