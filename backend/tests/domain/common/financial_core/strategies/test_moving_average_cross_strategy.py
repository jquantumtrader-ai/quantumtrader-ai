from decimal import Decimal

from app.domain.common.financial_core.strategies import (
    MovingAverageCrossStrategy,
)
from app.domain.common.financial_core.trading_signals import (
    TradingSignal,
)


def test_first_update_returns_hold() -> None:
    strategy = MovingAverageCrossStrategy()

    signal = strategy.update(
        fast=Decimal("10"),
        slow=Decimal("20"),
    )

    assert signal == TradingSignal.HOLD


def test_buy_signal_after_golden_cross() -> None:
    strategy = MovingAverageCrossStrategy()

    strategy.update(
        fast=Decimal("10"),
        slow=Decimal("20"),
    )

    signal = strategy.update(
        fast=Decimal("21"),
        slow=Decimal("20"),
    )

    assert signal == TradingSignal.BUY


def test_sell_signal_after_death_cross() -> None:
    strategy = MovingAverageCrossStrategy()

    strategy.update(
        fast=Decimal("20"),
        slow=Decimal("10"),
    )

    signal = strategy.update(
        fast=Decimal("9"),
        slow=Decimal("10"),
    )

    assert signal == TradingSignal.SELL


def test_hold_when_fast_remains_above() -> None:
    strategy = MovingAverageCrossStrategy()

    strategy.update(
        fast=Decimal("20"),
        slow=Decimal("10"),
    )

    signal = strategy.update(
        fast=Decimal("25"),
        slow=Decimal("10"),
    )

    assert signal == TradingSignal.HOLD


def test_hold_when_fast_remains_below() -> None:
    strategy = MovingAverageCrossStrategy()

    strategy.update(
        fast=Decimal("10"),
        slow=Decimal("20"),
    )

    signal = strategy.update(
        fast=Decimal("15"),
        slow=Decimal("20"),
    )

    assert signal == TradingSignal.HOLD


def test_buy_only_once_during_same_trend() -> None:
    strategy = MovingAverageCrossStrategy()

    strategy.update(
        fast=Decimal("10"),
        slow=Decimal("20"),
    )

    assert (
        strategy.update(
            fast=Decimal("21"),
            slow=Decimal("20"),
        )
        == TradingSignal.BUY
    )

    assert (
        strategy.update(
            fast=Decimal("30"),
            slow=Decimal("20"),
        )
        == TradingSignal.HOLD
    )

    assert (
        strategy.update(
            fast=Decimal("40"),
            slow=Decimal("20"),
        )
        == TradingSignal.HOLD
    )


def test_sell_only_once_during_same_trend() -> None:
    strategy = MovingAverageCrossStrategy()

    strategy.update(
        fast=Decimal("20"),
        slow=Decimal("10"),
    )

    assert (
        strategy.update(
            fast=Decimal("9"),
            slow=Decimal("10"),
        )
        == TradingSignal.SELL
    )

    assert (
        strategy.update(
            fast=Decimal("8"),
            slow=Decimal("10"),
        )
        == TradingSignal.HOLD
    )

    assert (
        strategy.update(
            fast=Decimal("7"),
            slow=Decimal("10"),
        )
        == TradingSignal.HOLD
    )
