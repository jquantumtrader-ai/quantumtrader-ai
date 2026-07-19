from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class FillResult:
    """
    Resultado de uma tentativa de preenchimento.
    """

    filled_quantity: Decimal

    remaining_quantity: Decimal

    completed: bool


class FillMatchingEngine:
    """
    Motor responsável pelo casamento
    entre quantidade solicitada e executada.
    """

    def match(
        self,
        requested_quantity: Decimal,
        current_filled_quantity: Decimal,
        fill_quantity: Decimal,
    ) -> FillResult:
        """
        Processa um novo preenchimento.
        """

        if requested_quantity <= Decimal("0"):
            raise ValueError(
                "Requested quantity must be positive"
            )

        if fill_quantity <= Decimal("0"):
            raise ValueError(
                "Fill quantity must be positive"
            )

        new_filled_quantity = (
            current_filled_quantity
            +
            fill_quantity
        )

        if new_filled_quantity > requested_quantity:
            raise ValueError(
                "Fill exceeds requested quantity"
            )

        remaining_quantity = (
            requested_quantity
            -
            new_filled_quantity
        )

        return FillResult(
            filled_quantity=new_filled_quantity,
            remaining_quantity=remaining_quantity,
            completed=(
                remaining_quantity
                ==
                Decimal("0")
            ),
        )
