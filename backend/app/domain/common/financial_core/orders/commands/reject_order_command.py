from __future__ import annotations

from dataclasses import dataclass

from .. import OrderId



@dataclass(
    frozen=True
)
class RejectOrderCommand:
    """
    Intenção de rejeição.
    """

    order_id: OrderId

    reason: str
