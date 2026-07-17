from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .positions.position import Position
from ..value_objects.money import Money


@dataclass
class Portfolio:
    """
    Aggregate raiz de uma carteira de investimentos.

    Controla o conjunto de posições pertencentes
    à carteira.
    """

    name: str

    _positions: list[Position] = field(
        default_factory=list,
        repr=False,
    )

    @property
    def positions(
        self,
    ) -> tuple[Position, ...]:
        """
        Retorna as posições em formato imutável.
        """

        return tuple(
            self._positions
        )

    def add_position(
        self,
        position: Position,
    ) -> None:
        """
        Adiciona uma posição ao portfolio.
        """

        self._positions.append(
            position
        )

    def remove_position(
        self,
        asset_symbol: str,
    ) -> None:
        """
        Remove uma posição pelo símbolo do ativo.
        """

        self._positions = [
            position
            for position in self._positions
            if position.asset.symbol
            != asset_symbol.upper()
        ]

    def total_cost(
        self,
    ) -> Money:
        """
        Calcula o custo total da carteira.
        """

        if not self._positions:
            raise ValueError(
                "Portfolio vazio."
            )

        currency = (
            self._positions[0]
            .average_price
            .currency
        )

        total = sum(
            (
                position.cost_basis.value
                for position in self._positions
            ),
            Decimal("0"),
        )

        return Money(
            total,
            currency,
        )

    def market_value(
        self,
        prices: dict[str, Money],
    ) -> Money:
        """
        Calcula valor de mercado atual.
        """

        if not self._positions:
            raise ValueError(
                "Portfolio vazio."
            )

        currency = (
            self._positions[0]
            .average_price
            .currency
        )

        total = Decimal("0")

        for position in self._positions:

            price = prices[
                position.asset.symbol
            ]

            total += (
                position.quantity
                *
                price.value
            )

        return Money(
            total,
            currency,
        )
