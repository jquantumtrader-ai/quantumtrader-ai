from __future__ import annotations

from datetime import datetime, timedelta

from ..candle_events import CandlePublisher
from ..candles import CandleBuilder
from ..market_data import MarketTick


class TimeCandleBuilder:
    """
    Fecha um candle quando o intervalo de tempo é atingido.
    """

    def __init__(
        self,
        interval: timedelta,
        publisher: CandlePublisher,
    ) -> None:
        if interval <= timedelta():
            raise ValueError("interval must be greater than zero")

        self._interval = interval
        self._publisher = publisher
        self._builder = CandleBuilder()
        self._period_start: datetime | None = None

    def update(self, tick: MarketTick) -> None:
        if self._period_start is None:
            self._period_start = tick.timestamp

        if tick.timestamp >= self._period_start + self._interval:
            candle = self._builder.candle

            if candle is not None:
                self._publisher.publish(candle)

            self._builder = CandleBuilder()
            self._period_start = tick.timestamp

        self._builder.update(tick)
