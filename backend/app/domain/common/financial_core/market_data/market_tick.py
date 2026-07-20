from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class MarketTick:
    """
    Representa um único tick recebido do mercado.
    """

    symbol: str
    price: Decimal
    volume: Decimal
    timestamp: datetime
