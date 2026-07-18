from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from .. import OrderId

from ...value_objects.money import Money



@dataclass(
    frozen=True
)
class FillOrderCommand:
    """
    Intenção de execução parcial
    ou total.
    """

    order_id: OrderId

    quantity: Decimal

    price: Money
