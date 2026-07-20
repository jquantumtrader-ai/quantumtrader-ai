from datetime import datetime
from decimal import Decimal

from app.domain.common.financial_core.candle_events import (
    InMemoryCandlePublisher,
)
from app.domain.common.financial_core.candles import Candle


def test_publish_candle() -> None:
    publisher = InMemoryCandlePublisher()

    received: list[Candle] = []

    publisher.subscribe(received.append)

    candle = Candle(
        symbol="WINQ26",
        open=Decimal("126000"),
        high=Decimal("126500"),
        low=Decimal("125900"),
        close=Decimal("126300"),
        volume=Decimal("15"),
        start_time=datetime.now(),
    )

    publisher.publish(candle)

    assert len(received) == 1
    assert received[0] == candle
