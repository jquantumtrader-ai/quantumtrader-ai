from uuid import uuid4

from app.domain.common.financial_core.orders.events import (
    OrderCancelled,
)

from app.domain.common.financial_core.orders import (
    OrderId,
)



def test_cancelled_event():

    event = OrderCancelled(
        OrderId(
            uuid4()
        )
    )


    assert (
        event.order_id
        is not None
    )
