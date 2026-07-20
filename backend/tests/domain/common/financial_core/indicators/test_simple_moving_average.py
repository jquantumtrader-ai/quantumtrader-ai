from datetime import datetime
from decimal import Decimal

from app.domain.common.financial_core.candles import Candle
from app.domain.common.financial_core.indicators import (
    SimpleMovingAverage,
)


def create_candle(close: str) -> Candle:
    value = Decimal(close)

    return Candle(
        symbol="WINQ26",
        open=value,
        high=value,
        low=value,
        close=value,
        volume=Decimal("1"),
        start_time=datetime.now(),
    )


def test_sma_is_not_ready_before_period() -> None:
    sma = SimpleMovingAverage(period=3)

    sma.update(create_candle("10"))
    sma.update(create_candle("20"))

    assert sma.is_ready is False
    assert sma.value is None


def test_sma_calculates_average() -> None:
    sma = SimpleMovingAverage(period=3)

    sma.update(create_candle("10"))
    sma.update(create_candle("20"))
    sma.update(create_candle("30"))

    assert sma.is_ready is True
    assert sma.value == Decimal("20")


def test_sma_sliding_window() -> None:
    sma = SimpleMovingAverage(period=3)

    sma.update(create_candle("10"))
    sma.update(create_candle("20"))
    sma.update(create_candle("30"))

    assert sma.value == Decimal("20")

    sma.update(create_candle("40"))

    assert sma.value == Decimal("30")


def test_invalid_period() -> None:
    try:
        SimpleMovingAverage(period=0)
        assert False
    except ValueError:
        assert True
