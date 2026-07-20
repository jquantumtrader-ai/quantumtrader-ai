from __future__ import annotations

from collections.abc import Callable

from ..candles import Candle
from .candle_publisher import CandlePublisher


class InMemoryCandlePublisher(CandlePublisher):
    """
    Publicador de candles em memória.
    """

    def __init__(self) -> None:
        self._subscribers: list[Callable[[Candle], None]] = []

    def subscribe(
        self,
        callback: Callable[[Candle], None],
    ) -> None:
        self._subscribers.append(callback)

    def publish(self, candle: Candle) -> None:
        for subscriber in self._subscribers:
            subscriber(candle)
