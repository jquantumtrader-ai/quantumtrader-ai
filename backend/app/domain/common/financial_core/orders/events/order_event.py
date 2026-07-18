from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..order_id import OrderId



@dataclass(frozen=True)
class OrderEvent:
    """
    Evento base de domínio
    relacionado a uma ordem.
    """


    order_id: OrderId

    occurred_at: datetime
