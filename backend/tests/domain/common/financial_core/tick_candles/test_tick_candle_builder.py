from datetime import datetime
from decimal import Decimal

from app.domain.common.financial_core.candle_events import (
    InMemoryCandlePublisher,
)
from app.domain.common.financial_core.market_data import (
    MarketTick,
)
from app.domain.common.financial_core.tick_candles import (
    TickCandleBuilder,
)


def test_publish_candle_after_tick_limit() -> None:
    publisher = InMemoryCandlePublisher()

    received = []

    publisher.subscribe(received.append)

    builder = TickCandleBuilder(
        ticks_per_candle=3,
        publisher=publisher,
    )

    for price in (
        Decimal("100"),
        Decimal("101"),
        Decimal("99"),
    ):
        builder.update(
            MarketTick(
                symbol="WINQ26",
                price=price,
                volume=Decimal("1"),
                timestamp=datetime.now(),
            )
        )

    assert len(received) == 1

    candle = received[0]

    assert candle.open == Decimal("100")
    assert candle.high == Decimal("101")
    assert candle.low == Decimal("99")
    assert candle.close == Decimal("99")
    assert candle.volume == Decimal("3")


def test_do_not_publish_before_tick_limit() -> None:
    publisher = InMemoryCandlePublisher()

    received = []

    publisher.subscribe(received.append)

    builder = TickCandleBuilder(
        ticks_per_candle=3,
        publisher=publisher,
    )

    for price in (
        Decimal("100"),
        Decimal("101"),
    ):
        builder.update(
            MarketTick(
                symbol="WINQ26",
                price=price,
                volume=Decimal("1"),
                timestamp=datetime.now(),
            )
        )

    assert received == []
