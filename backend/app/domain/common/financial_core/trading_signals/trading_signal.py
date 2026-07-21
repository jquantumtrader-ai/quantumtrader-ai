from __future__ import annotations

from enum import Enum


class TradingSignal(str, Enum):
    """
    Representa um sinal de negociação produzido por uma estratégia.
    """

    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
