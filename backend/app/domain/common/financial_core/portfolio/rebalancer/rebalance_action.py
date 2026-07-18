from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ...value_objects.money import Money
from ..assets.asset import Asset


@dataclass(frozen=True)
class RebalanceAction:
    """
    Representa uma ação necessária para rebalancear
    uma posição da carteira.
    """

    asset: Asset

    current_quantity: Decimal

    target_quantity: Decimal

    quantity_difference: Decimal

    current_weight: Decimal

    target_weight: Decimal

    current_value: Money

    target_value: Money

    value_difference: Money

    @property
    def is_buy(self) -> bool:
        return self.quantity_difference > Decimal("0")

    @property
    def is_sell(self) -> bool:
        return self.quantity_difference < Decimal("0")

    @property
    def is_hold(self) -> bool:
        return self.quantity_difference == Decimal("0")
