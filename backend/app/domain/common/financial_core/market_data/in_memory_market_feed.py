from __future__ import annotations

from collections.abc import Callable

from .market_feed import MarketFeed
from .market_tick import MarketTick


class InMemoryMarketFeed(MarketFeed):
    """
    Implementação em memória de um MarketFeed.
    """

    def __init__(self) -> None:
        self._subscribers: list[Callable[[MarketTick], None]] = []

    def subscribe(
        self,
        callback: Callable[[MarketTick], None],
    ) -> None:
        self._subscribers.append(callback)

    def publish(self, tick: MarketTick) -> None:
        for subscriber in self._subscribers:
            subscriber(tick)
