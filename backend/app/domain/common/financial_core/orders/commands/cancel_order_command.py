from __future__ import annotations

from dataclasses import dataclass

from .. import OrderId



@dataclass(
    frozen=True
)
class CancelOrderCommand:
    """
    Intenção de cancelamento.
    """

    order_id: OrderId
