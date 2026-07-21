from datetime import datetime
from decimal import Decimal

from app.domain.common.financial_core.candles import Candle
from app.domain.common.financial_core.indicators import (
    ExponentialMovingAverage,
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


def test_invalid_period() -> None:
    try:
        ExponentialMovingAverage(period=0)
        assert False
    except ValueError:
        assert True


def test_first_value_is_first_close() -> None:
    ema = ExponentialMovingAverage(period=3)

    ema.update(create_candle("10"))

    assert ema.is_ready is True
    assert ema.value == Decimal("10")


def test_ema_updates_after_new_candle() -> None:
    ema = ExponentialMovingAverage(period=3)

    ema.update(create_candle("10"))
    ema.update(create_candle("20"))

    expected = Decimal("15")

    assert ema.value == expected


def test_ema_keeps_updating() -> None:
    ema = ExponentialMovingAverage(period=3)

    ema.update(create_candle("10"))
    ema.update(create_candle("20"))
    ema.update(create_candle("30"))

    assert ema.value == Decimal("22.5")
