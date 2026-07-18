from app.domain.common.financial_core.orders.aggregate import (
    OrderAggregate,
)

from app.domain.common.financial_core.orders.events import (
    OrderCreated,
    OrderFilled,
    OrderCancelled,
    OrderRejected,
)


from tests.orders.entities.test_order import (
    create_order,
)



def create_aggregate():

    return OrderAggregate(
        create_order()
    )



def test_created_event():

    aggregate = create_aggregate()


    aggregate.created()


    events = aggregate.pull_events()


    assert len(events) == 1

    assert isinstance(
        events[0],
        OrderCreated,
    )



def test_filled_event():

    aggregate = create_aggregate()


    aggregate.filled()


    events = aggregate.pull_events()


    assert isinstance(
        events[0],
        OrderFilled,
    )



def test_cancelled_event():

    aggregate = create_aggregate()


    aggregate.cancelled()


    events = aggregate.pull_events()


    assert isinstance(
        events[0],
        OrderCancelled,
    )



def test_rejected_event():

    aggregate = create_aggregate()


    aggregate.rejected()


    events = aggregate.pull_events()


    assert isinstance(
        events[0],
        OrderRejected,
    )



def test_pull_events_clears_queue():

    aggregate = create_aggregate()


    aggregate.created()


    aggregate.pull_events()


    assert (
        len(
            aggregate.pull_events()
        )
        ==
        0
    )
