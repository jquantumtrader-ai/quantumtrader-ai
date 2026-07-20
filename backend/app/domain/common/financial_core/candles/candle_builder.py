from __future__ import annotations

from .candle import Candle
from ..market_data import MarketTick


class CandleBuilder:
    """
    Constrói um candle a partir de uma sequência de ticks.
    """

    def __init__(self) -> None:
        self._candle: Candle | None = None

    @property
    def candle(self) -> Candle | None:
        return self._candle

    def update(self, tick: MarketTick) -> Candle:
        if self._candle is None:
            self._candle = Candle(
                symbol=tick.symbol,
                open=tick.price,
                high=tick.price,
                low=tick.price,
                close=tick.price,
                volume=tick.volume,
                start_time=tick.timestamp,
            )
            return self._candle

        self._candle.update(
            price=tick.price,
            volume=tick.volume,
        )

        return self._candle
