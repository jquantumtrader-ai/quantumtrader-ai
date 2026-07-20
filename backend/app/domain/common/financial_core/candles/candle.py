from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(slots=True)
class Candle:
    """
    Representa um candle OHLCV.
    """

    symbol: str
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    start_time: datetime

    def update(
        self,
        price: Decimal,
        volume: Decimal,
    ) -> None:
        if price > self.high:
            self.high = price

        if price < self.low:
            self.low = price

        self.close = price
        self.volume += volume
