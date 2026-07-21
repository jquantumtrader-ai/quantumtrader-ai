from __future__ import annotations

from decimal import Decimal

from app.domain.common.financial_core.trading_signals import TradingSignal


class MovingAverageCrossStrategy:
    """
    Estratégia baseada no cruzamento entre uma média rápida e uma média lenta.

    Emite um sinal apenas quando ocorre um cruzamento efetivo.
    """

    def __init__(self) -> None:
        self._previous_fast_above_slow: bool | None = None

    def update(
        self,
        fast: Decimal,
        slow: Decimal,
    ) -> TradingSignal:
        current_fast_above_slow = fast > slow

        if self._previous_fast_above_slow is None:
            self._previous_fast_above_slow = current_fast_above_slow
            return TradingSignal.HOLD

        if (
            not self._previous_fast_above_slow
            and current_fast_above_slow
        ):
            self._previous_fast_above_slow = current_fast_above_slow
            return TradingSignal.BUY

        if (
            self._previous_fast_above_slow
            and not current_fast_above_slow
        ):
            self._previous_fast_above_slow = current_fast_above_slow
            return TradingSignal.SELL

        self._previous_fast_above_slow = current_fast_above_slow
        return TradingSignal.HOLD
