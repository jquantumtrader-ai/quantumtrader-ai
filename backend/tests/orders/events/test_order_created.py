from uuid import uuid4

from app.domain.common.financial_core.orders.events import (
    OrderCreated,
)

from app.domain.common.financial_core.orders import (
    OrderId,
)



def test_created_event():

    event = OrderCreated(
        OrderId(
            uuid4()
        )
    )


    assert (
        event.order_id
        is not None
    )
