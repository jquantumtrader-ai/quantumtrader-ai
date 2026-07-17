from __future__ import annotations

from decimal import Decimal

from ..portfolio import Portfolio
from ...value_objects.money import Money


class PortfolioMetrics:
    """
    Serviços de cálculo de métricas financeiras
    de uma carteira.
    """

    def __init__(
        self,
        portfolio: Portfolio,
    ) -> None:

        self.portfolio = portfolio


    def total_cost(self) -> Money:
        """
        Retorna o custo total de aquisição
        da carteira.
        """

        return self.portfolio.total_cost()


    def market_value(
        self,
        prices: dict[str, Money],
    ) -> Money:
        """
        Calcula o valor atual da carteira.
        """

        return self.portfolio.market_value(
            prices,
        )


    def unrealized_pnl(
        self,
        prices: dict[str, Money],
    ) -> Money:
        """
        Calcula lucro/prejuízo não realizado.

        Fórmula:

        valor atual - custo de aquisição
        """

        current_value = self.market_value(
            prices,
        )

        cost = self.total_cost()

        return current_value - cost


    def allocation_weights(
        self,
        prices: dict[str, Money],
    ) -> dict[str, Decimal]:
        """
        Calcula o peso percentual de cada ativo
        dentro da carteira.
        """

        total = self.market_value(
            prices,
        )

        if total.value == Decimal("0"):
            raise ValueError(
                "Não é possível calcular pesos de uma carteira vazia."
            )

        weights: dict[str, Decimal] = {}

        for position in self.portfolio.positions:

            symbol = position.asset.symbol

            value = (
                prices[symbol].value
                *
                position.quantity
            )

            weights[symbol] = (
                value
                / total.value
            )

        return weights
