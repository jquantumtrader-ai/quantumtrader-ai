from __future__ import annotations

from decimal import Decimal

from ...value_objects.money import Money
from ..analytics.analytics import PortfolioAnalytics
from ..portfolio import Portfolio
from .rebalance_action import RebalanceAction
from .rebalance_plan import RebalancePlan


class PortfolioRebalancer:
    """
    Serviço responsável pelo cálculo
    de rebalanceamento de carteira.
    """

    def __init__(
        self,
        portfolio: Portfolio,
    ) -> None:

        self._portfolio = portfolio

        self._analytics = PortfolioAnalytics(
            portfolio,
        )

    @property
    def portfolio(
        self,
    ) -> Portfolio:

        return self._portfolio

    def total_market_value(
        self,
        prices: dict[str, Money],
    ) -> Money:

        return self._analytics.total_market_value(
            prices,
        )

    def current_weights(
        self,
        prices: dict[str, Money],
    ) -> dict[str, Decimal]:

        return self._analytics.weights(
            prices,
        )

    def rebalance(
        self,
        prices: dict[str, Money],
        target_weights: dict[str, Decimal],
    ) -> RebalancePlan:

        actions: list[
            RebalanceAction
        ] = []

        total = self.total_market_value(
            prices,
        )

        current = self.current_weights(
            prices,
        )

        for position in self.portfolio.positions:

            symbol = position.asset.symbol

            target_weight = (
                target_weights[
                    symbol
                ]
            )

            current_weight = (
                current[
                    symbol
                ]
            )

            current_price = prices[
                symbol
            ]

            current_value = (
                position.market_value(
                    current_price,
                )
            )

            target_value = Money(
                total.value
                * target_weight,
                total.currency,
            )

            quantity_target = (
                target_value.value
                /
                current_price.value
            )

            quantity_difference = (
                quantity_target
                -
                position.quantity
            )

            value_difference = Money(
                target_value.value
                -
                current_value.value,
                total.currency,
            )

            actions.append(
                RebalanceAction(
                    asset=position.asset,

                    current_quantity=(
                        position.quantity
                    ),

                    target_quantity=(
                        quantity_target
                    ),

                    quantity_difference=(
                        quantity_difference
                    ),

                    current_weight=(
                        current_weight
                    ),

                    target_weight=(
                        target_weight
                    ),

                    current_value=(
                        current_value
                    ),

                    target_value=(
                        target_value
                    ),

                    value_difference=(
                        value_difference
                    ),
                )
            )

        return RebalancePlan(
            actions,
        )
