from uuid import uuid4

from app.domain.common.financial_core.orders import (
    OrderId,
)

from app.domain.common.financial_core.orders.events import (
    OrderCreated,
)

from app.domain.common.financial_core.orders.events.dispatcher import (
    OrderEventDispatcher,
)



def test_register_and_dispatch():

    dispatcher = OrderEventDispatcher()


    received = []


    def handler(event):

        received.append(
            event
        )


    dispatcher.register(
        OrderCreated,
        handler,
    )


    event = OrderCreated(
        OrderId(
            uuid4()
        )
    )


    dispatcher.dispatch(
        event
    )


    assert (
        len(received)
        ==
        1
    )


    assert (
        received[0]
        ==
        event
    )



def test_multiple_handlers():

    dispatcher = OrderEventDispatcher()


    counter = {
        "value": 0
    }


    def handler_one(event):

        counter["value"] += 1


    def handler_two(event):

        counter["value"] += 1



    dispatcher.register(
        OrderCreated,
        handler_one,
    )


    dispatcher.register(
        OrderCreated,
        handler_two,
    )


    dispatcher.dispatch(
        OrderCreated(
            OrderId(
                uuid4()
            )
        )
    )


    assert (
        counter["value"]
        ==
        2
    )



def test_clear_handlers():

    dispatcher = OrderEventDispatcher()


    dispatcher.register(
        OrderCreated,
        lambda event: None,
    )


    dispatcher.clear()


    assert (
        len(
            dispatcher._handlers
        )
        ==
        0
    )
