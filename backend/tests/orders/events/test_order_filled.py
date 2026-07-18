from uuid import uuid4

from app.domain.common.financial_core.orders.events import (
    OrderFilled,
)

from app.domain.common.financial_core.orders import (
    OrderId,
)



def test_filled_event():

    event = OrderFilled(
        OrderId(
            uuid4()
        )
    )


    assert (
        event.order_id
        is not None
    )
