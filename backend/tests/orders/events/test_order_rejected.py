from uuid import uuid4

from app.domain.common.financial_core.orders.events import (
    OrderRejected,
)

from app.domain.common.financial_core.orders import (
    OrderId,
)



def test_rejected_event():

    event = OrderRejected(
        OrderId(
            uuid4()
        )
    )


    assert (
        event.order_id
        is not None
    )
