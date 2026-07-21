from __future__ import annotations

from decimal import Decimal

from ..candles import Candle


class ExponentialMovingAverage:
    """
    Calcula a Média Móvel Exponencial (EMA)
    utilizando o preço de fechamento dos candles.
    """

    def __init__(self, period: int) -> None:
        if period <= 0:
            raise ValueError("period must be greater than zero")

        self._period = period
        self._multiplier = Decimal("2") / Decimal(period + 1)
        self._value: Decimal | None = None

    def update(self, candle: Candle) -> None:
        close = candle.close

        if self._value is None:
            self._value = close
            return

        self._value = (
            (close - self._value) * self._multiplier
        ) + self._value

    @property
    def value(self) -> Decimal | None:
        return self._value

    @property
    def is_ready(self) -> bool:
        return self._value is not None

    @property
    def period(self) -> int:
        return self._period
