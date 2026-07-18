from __future__ import annotations

from decimal import Decimal

from ..performance import PortfolioPerformance
from ..portfolio import Portfolio
from ...value_objects.money import Money


class PortfolioAnalytics:
    """
    Métricas analíticas de uma carteira.
    """

    def __init__(
        self,
        portfolio: Portfolio,
    ) -> None:

        self._portfolio = portfolio
        self._performance = PortfolioPerformance(
            portfolio,
        )

    def total_market_value(
        self,
        prices: dict[str, Money],
    ) -> Money:

        return self._performance.market_value(
            prices,
        )

    def weights(
        self,
        prices: dict[str, Money],
    ) -> dict[str, Decimal]:

        total = self.total_market_value(
            prices,
        )

        if total.value == Decimal("0"):
            return {}

        result: dict[str, Decimal] = {}

        for position in self._portfolio.positions:

            market_value = position.market_value(
                prices[
                    position.asset.symbol
                ]
            )

            result[
                position.asset.symbol
            ] = (
                market_value.value
                / total.value
            )

        return result

    def concentration(
        self,
        prices: dict[str, Money],
    ) -> Decimal:

        weights = self.weights(
            prices,
        )

        if not weights:
            return Decimal("0")

        return max(
            weights.values(),
        )

    def largest_position(
        self,
        prices: dict[str, Money],
    ) -> str | None:

        weights = self.weights(
            prices,
        )

        if not weights:
            return None

        largest_symbol: str | None = None
        largest_weight = Decimal("-1")

        for symbol, weight in weights.items():

            if weight > largest_weight:
                largest_weight = weight
                largest_symbol = symbol

        return largest_symbol

    def smallest_position(
        self,
        prices: dict[str, Money],
    ) -> str | None:

        weights = self.weights(
            prices,
        )

        if not weights:
            return None

        smallest_symbol: str | None = None
        smallest_weight = Decimal("999999999")

        for symbol, weight in weights.items():

            if weight < smallest_weight:
                smallest_weight = weight
                smallest_symbol = symbol

        return smallest_symbol

    def is_concentrated(
        self,
        prices: dict[str, Money],
        limit: Decimal = Decimal("0.50"),
    ) -> bool:

        return (
            self.concentration(
                prices,
            )
            > limit
        )

    def diversification_index(
        self,
        prices: dict[str, Money],
    ) -> Decimal:
        """
        Índice simples de diversificação
        (1 - HHI).
        """

        weights = self.weights(
            prices,
        )

        if not weights:
            return Decimal("0")

        return Decimal("1") - sum(
            (
                weight * weight
                for weight in weights.values()
            ),
            Decimal("0"),
        )
