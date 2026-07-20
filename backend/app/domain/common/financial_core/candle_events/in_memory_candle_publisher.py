from __future__ import annotations

from collections.abc import Callable

from ..candles import Candle
from .candle_publisher import CandlePublisher


class InMemoryCandlePublisher(CandlePublisher):
    def __init__(self) -> None:
        self._subscribers: list[Callable[[Candle], None]] = []

    def subscribe(
        self,
        subscriber: Callable[[Candle], None],
    ) -> None:
        self._subscribers.append(subscriber)

    def publish(self, candle: Candle) -> None:
        for subscriber in self._subscribers:
            subscriber(candle)
