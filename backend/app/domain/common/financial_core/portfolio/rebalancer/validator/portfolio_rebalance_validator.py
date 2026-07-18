from __future__ import annotations

from decimal import Decimal

from ....value_objects.money import Money
from ...portfolio import Portfolio


class PortfolioRebalanceValidator:
    """
    Responsável por validar uma operação
    de rebalanceamento antes da geração do plano.
    """

    def validate(
        self,
        portfolio: Portfolio,
        prices: dict[str, Money],
        target_weights: dict[str, Decimal],
    ) -> None:

        if not portfolio.positions:
            raise ValueError(
                "Portfolio vazio."
            )

        if not target_weights:
            raise ValueError(
                "Pesos alvo não informados."
            )

        total_weight = sum(
            target_weights.values(),
            Decimal("0"),
        )

        if total_weight != Decimal("1"):
            raise ValueError(
                "Os pesos devem somar 1."
            )

        portfolio_symbols = {
            position.asset.symbol
            for position in portfolio.positions
        }

        target_symbols = set(
            target_weights.keys()
        )

        if portfolio_symbols != target_symbols:
            raise ValueError(
                "Ativos da carteira e pesos alvo são diferentes."
            )

        for symbol, weight in target_weights.items():

            if weight < Decimal("0"):
                raise ValueError(
                    f"Peso negativo para {symbol}."
                )

            if symbol not in prices:
                raise ValueError(
                    f"Preço não encontrado para {symbol}."
                )

            if prices[symbol].value <= Decimal("0"):
                raise ValueError(
                    f"Preço inválido para {symbol}."
                )
