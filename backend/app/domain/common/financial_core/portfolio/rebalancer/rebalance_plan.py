from __future__ import annotations

from dataclasses import dataclass, field

from .rebalance_action import RebalanceAction


@dataclass(frozen=True)
class RebalancePlan:
    """
    Plano completo de rebalanceamento.
    """

    actions: list[RebalanceAction] = field(
        default_factory=list,
    )

    @property
    def buy_actions(
        self,
    ) -> list[RebalanceAction]:

        return [
            action
            for action in self.actions
            if action.is_buy
        ]

    @property
    def sell_actions(
        self,
    ) -> list[RebalanceAction]:

        return [
            action
            for action in self.actions
            if action.is_sell
        ]

    @property
    def hold_actions(
        self,
    ) -> list[RebalanceAction]:

        return [
            action
            for action in self.actions
            if action.is_hold
        ]
