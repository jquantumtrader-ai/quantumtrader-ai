from __future__ import annotations

from dataclasses import dataclass

from ..execution.execution_intent import ExecutionIntent
from ..execution.intent_type import IntentType
from ..rebalance_plan import RebalancePlan


@dataclass(frozen=True)
class RebalanceReport:
    """
    Relatório resumido do rebalanceamento.
    """

    plan: RebalancePlan

    @property
    def execution_intents(
        self,
    ) -> list[ExecutionIntent]:

        return [
            ExecutionIntent.from_action(action)
            for action in self.plan.actions
        ]

    @property
    def buy_orders(
        self,
    ) -> list[ExecutionIntent]:

        return [
            intent
            for intent in self.execution_intents
            if intent.intent_type is IntentType.BUY
        ]

    @property
    def sell_orders(
        self,
    ) -> list[ExecutionIntent]:

        return [
            intent
            for intent in self.execution_intents
            if intent.intent_type is IntentType.SELL
        ]

    @property
    def hold_orders(
        self,
    ) -> list[ExecutionIntent]:

        return [
            intent
            for intent in self.execution_intents
            if intent.intent_type is IntentType.HOLD
        ]

    @property
    def total_orders(
        self,
    ) -> int:

        return len(
            self.execution_intents,
        )

    @property
    def total_buy_orders(
        self,
    ) -> int:

        return len(
            self.buy_orders,
        )

    @property
    def total_sell_orders(
        self,
    ) -> int:

        return len(
            self.sell_orders,
        )

    @property
    def total_hold_orders(
        self,
    ) -> int:

        return len(
            self.hold_orders,
        )
