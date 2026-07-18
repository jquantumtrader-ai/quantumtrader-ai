from __future__ import annotations

from datetime import datetime

from .order_event import OrderEvent



class OrderRejected(OrderEvent):
    """
    Evento disparado quando uma ordem
    é rejeitada.
    """


    def __init__(
        self,
        order_id,
    ):

        super().__init__(
            order_id=order_id,
            occurred_at=datetime.utcnow(),
        )
