from __future__ import annotations

from app.domain.common.financial_core.trading_signals import TradingSignal


class PaperExecution:
    """
    Executa sinais de negociação sobre uma posição simulada.

    Estado possível:
        - FLAT (sem posição)
        - LONG (posição comprada)
    """

    def __init__(self) -> None:
        self._is_long = False

    def execute(self, signal: TradingSignal) -> None:
        if signal is TradingSignal.BUY:
            self._is_long = True
            return

        if signal is TradingSignal.SELL:
            self._is_long = False

    @property
    def is_long(self) -> bool:
        return self._is_long

    @property
    def is_flat(self) -> bool:
        return not self._is_long
