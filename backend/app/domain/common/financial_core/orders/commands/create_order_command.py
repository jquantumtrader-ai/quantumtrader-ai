from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ...portfolio.assets.asset import Asset
from ...value_objects.money import Money
from ..enums import OrderSide, OrderType



@dataclass(
    frozen=True
)
class CreateOrderCommand:
    """
    Intenção de criação de uma ordem.
    """

    asset: Asset

    side: OrderSide

    order_type: OrderType

    quantity: Decimal

    price: Money
