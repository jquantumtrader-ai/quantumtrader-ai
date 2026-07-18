from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..rebalance_action import RebalanceAction
from .intent_type import IntentType


@dataclass(
    frozen=True
)
class ExecutionIntent:
    """
    Representa uma intenção operacional
    gerada pelo rebalanceamento.
    """

    action: RebalanceAction

    intent_type: IntentType

    quantity: Decimal


    def __post_init__(self) -> None:

        if self.quantity < Decimal("0"):
            raise ValueError(
                "Quantidade da intenção não pode ser negativa."
            )


    @classmethod
    def from_action(
        cls,
        action: RebalanceAction,
    ) -> ExecutionIntent:
        """
        Converte uma ação de rebalanceamento
        em intenção de execução.
        """

        difference = (
            action.quantity_difference
        )


        if difference > Decimal("0"):

            return cls(
                action=action,
                intent_type=IntentType.BUY,
                quantity=difference,
            )


        if difference < Decimal("0"):

            return cls(
                action=action,
                intent_type=IntentType.SELL,
                quantity=abs(difference),
            )


        return cls(
            action=action,
            intent_type=IntentType.HOLD,
            quantity=Decimal("0"),
        )
