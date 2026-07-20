from __future__ import annotations

from collections import deque
from decimal import Decimal

from ..candles import Candle


class SimpleMovingAverage:
    """
    Calcula a Média Móvel Simples (SMA) sobre o fechamento dos candles.
    """

    def __init__(self, period: int) -> None:
        if period <= 0:
            raise ValueError("period must be greater than zero")

        self._period = period
        self._values: deque[Decimal] = deque(maxlen=period)
        self._value: Decimal | None = None

    def update(self, candle: Candle) -> None:
        self._values.append(candle.close)

        if len(self._values) == self._period:
            self._value = sum(self._values, Decimal("0")) / Decimal(self._period)

    @property
    def value(self) -> Decimal | None:
        return self._value

    @property
    def is_ready(self) -> bool:
        return self._value is not None

    @property
    def period(self) -> int:
        return self._period
