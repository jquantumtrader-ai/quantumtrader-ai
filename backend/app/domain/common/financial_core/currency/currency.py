from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Currency:
    """
    Representa uma moeda negociável.
    """

    code: str
    symbol: str
    name: str

    def __str__(self) -> str:
        return self.code


BRL = Currency(
    code="BRL",
    symbol="R$",
    name="Brazilian Real",
)

USD = Currency(
    code="USD",
    symbol="$",
    name="US Dollar",
)

EUR = Currency(
    code="EUR",
    symbol="€",
    name="Euro",
)

BTC = Currency(
    code="BTC",
    symbol="₿",
    name="Bitcoin",
)

ETH = Currency(
    code="ETH",
    symbol="Ξ",
    name="Ethereum",
)
