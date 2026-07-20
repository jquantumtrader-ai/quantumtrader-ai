from __future__ import annotations

from ..candle_events import CandlePublisher
from ..candles import CandleBuilder
from ..market_data import MarketTick


class TickCandleBuilder:
    """
    Fecha um candle após uma quantidade fixa de ticks.
    """

    def __init__(
        self,
        ticks_per_candle: int,
        publisher: CandlePublisher,
    ) -> None:
        if ticks_per_candle <= 0:
            raise ValueError("ticks_per_candle must be greater than zero")

        self._ticks_per_candle = ticks_per_candle
        self._publisher = publisher
        self._builder = CandleBuilder()
        self._tick_count = 0

    def update(self, tick: MarketTick) -> None:
        candle = self._builder.update(tick)

        self._tick_count += 1

        if self._tick_count < self._ticks_per_candle:
            return

        self._publisher.publish(candle)

        self._builder = CandleBuilder()
        self._tick_count = 0
