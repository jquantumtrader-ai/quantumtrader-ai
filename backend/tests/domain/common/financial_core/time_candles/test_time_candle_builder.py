from datetime import datetime, timedelta
from decimal import Decimal

from app.domain.common.financial_core.candle_events import (
    InMemoryCandlePublisher,
)
from app.domain.common.financial_core.market_data import (
    MarketTick,
)
from app.domain.common.financial_core.time_candles import (
    TimeCandleBuilder,
)


def test_publish_candle_after_time_interval() -> None:
    publisher = InMemoryCandlePublisher()

    received = []

    publisher.subscribe(received.append)

    builder = TimeCandleBuilder(
        interval=timedelta(minutes=1),
        publisher=publisher,
    )

    start = datetime(2026, 1, 1, 9, 0, 0)

    builder.update(
        MarketTick(
            symbol="WIN",
            price=Decimal("100"),
            volume=Decimal("1"),
            timestamp=start,
        )
    )

    builder.update(
        MarketTick(
            symbol="WIN",
            price=Decimal("101"),
            volume=Decimal("1"),
            timestamp=start + timedelta(seconds=30),
        )
    )

    builder.update(
        MarketTick(
            symbol="WIN",
            price=Decimal("102"),
            volume=Decimal("1"),
            timestamp=start + timedelta(minutes=1),
        )
    )

    assert len(received) == 1

    candle = received[0]

    assert candle.open == Decimal("100")
    assert candle.high == Decimal("101")
    assert candle.low == Decimal("100")
    assert candle.close == Decimal("101")
    assert candle.volume == Decimal("2")


def test_do_not_publish_before_interval() -> None:
    publisher = InMemoryCandlePublisher()

    received = []

    publisher.subscribe(received.append)

    builder = TimeCandleBuilder(
        interval=timedelta(minutes=1),
        publisher=publisher,
    )

    start = datetime(2026, 1, 1, 9, 0, 0)

    builder.update(
        MarketTick(
            symbol="WIN",
            price=Decimal("100"),
            volume=Decimal("1"),
            timestamp=start,
        )
    )

    builder.update(
        MarketTick(
            symbol="WIN",
            price=Decimal("101"),
            volume=Decimal("1"),
            timestamp=start + timedelta(seconds=50),
        )
    )

    assert received == []
