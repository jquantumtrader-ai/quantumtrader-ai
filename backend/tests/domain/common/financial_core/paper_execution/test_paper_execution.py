from app.domain.common.financial_core.paper_execution import (
    PaperExecution,
)
from app.domain.common.financial_core.trading_signals import (
    TradingSignal,
)


def test_initial_state_is_flat() -> None:
    execution = PaperExecution()

    assert execution.is_flat
    assert not execution.is_long


def test_buy_opens_position() -> None:
    execution = PaperExecution()

    execution.execute(TradingSignal.BUY)

    assert execution.is_long
    assert not execution.is_flat


def test_buy_when_already_long_keeps_position() -> None:
    execution = PaperExecution()

    execution.execute(TradingSignal.BUY)
    execution.execute(TradingSignal.BUY)

    assert execution.is_long


def test_sell_closes_position() -> None:
    execution = PaperExecution()

    execution.execute(TradingSignal.BUY)
    execution.execute(TradingSignal.SELL)

    assert execution.is_flat
    assert not execution.is_long


def test_sell_when_flat_keeps_flat() -> None:
    execution = PaperExecution()

    execution.execute(TradingSignal.SELL)

    assert execution.is_flat
    assert not execution.is_long


def test_hold_does_not_change_state() -> None:
    execution = PaperExecution()

    execution.execute(TradingSignal.HOLD)

    assert execution.is_flat

    execution.execute(TradingSignal.BUY)
    execution.execute(TradingSignal.HOLD)

    assert execution.is_long
