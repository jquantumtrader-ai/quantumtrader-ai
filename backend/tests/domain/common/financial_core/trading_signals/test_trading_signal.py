from app.domain.common.financial_core.trading_signals import (
    TradingSignal,
)


def test_buy_signal() -> None:
    assert TradingSignal.BUY.value == "BUY"


def test_sell_signal() -> None:
    assert TradingSignal.SELL.value == "SELL"


def test_hold_signal() -> None:
    assert TradingSignal.HOLD.value == "HOLD"


def test_all_signals_are_unique() -> None:
    values = {signal.value for signal in TradingSignal}

    assert values == {
        "BUY",
        "SELL",
        "HOLD",
    }
