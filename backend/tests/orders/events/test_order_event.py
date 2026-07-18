from datetime import datetime
from uuid import uuid4

from app.domain.common.financial_core.orders.events import (
    OrderEvent,
)

from app.domain.common.financial_core.orders import (
    OrderId,
)



def test_order_event_creation():

    event = OrderEvent(
        order_id=OrderId(
            uuid4()
        ),
        occurred_at=datetime.utcnow(),
    )


    assert (
        event.order_id
        is not None
    )
