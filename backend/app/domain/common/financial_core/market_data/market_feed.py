from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable

from .market_tick import MarketTick


class MarketFeed(ABC):
    """
    Contrato para distribuição de ticks de mercado.
    """

    @abstractmethod
    def publish(self, tick: MarketTick) -> None:
        ...

    @abstractmethod
    def subscribe(
        self,
        callback: Callable[[MarketTick], None],
    ) -> None:
        ...
