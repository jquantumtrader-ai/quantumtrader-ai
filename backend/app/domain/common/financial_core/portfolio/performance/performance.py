from __future__ import annotations

from decimal import Decimal

from ..portfolio import Portfolio
from ...value_objects.money import Money


class PortfolioPerformance:
    """
    Calcula métricas básicas de performance
    de uma carteira.

    Esta classe será a base para:

    - Sharpe Ratio
    - Sortino Ratio
    - Drawdown
    - CAGR
    - Alpha
    - Beta
    """

    def __init__(
        self,
        portfolio: Portfolio,
    ) -> None:

        self._portfolio = portfolio

    def invested_capital(self) -> Money:
        """
        Capital investido.
        """

        return self._portfolio.total_cost()

    def market_value(
        self,
        prices: dict[str, Money],
    ) -> Money:
        """
        Valor atual.
        """

        return self._portfolio.market_value(
            prices,
        )

    def profit_loss(
        self,
        prices: dict[str, Money],
    ) -> Money:
        """
        Lucro/prejuízo absoluto.
        """

        return (
            self.market_value(prices)
            - self.invested_capital()
        )

    def return_percentage(
        self,
        prices: dict[str, Money],
    ) -> Decimal:
        """
        Retorno percentual.

        retorno = lucro / capital
        """

        invested = self.invested_capital()

        if invested.value == Decimal("0"):
            return Decimal("0")

        pnl = self.profit_loss(
            prices,
        )

        return (
            pnl.value
            / invested.value
        )

    def is_profitable(
        self,
        prices: dict[str, Money],
    ) -> bool:
        """
        Retorna True se houver lucro.
        """

        return (
            self.profit_loss(
                prices,
            ).value
            > Decimal("0")
        )

    def is_loss(
        self,
        prices: dict[str, Money],
    ) -> bool:
        """
        Retorna True se houver prejuízo.
        """

        return (
            self.profit_loss(
                prices,
            ).value
            < Decimal("0")
        )
