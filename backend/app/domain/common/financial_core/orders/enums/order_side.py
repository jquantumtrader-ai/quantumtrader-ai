from __future__ import annotations

from enum import Enum


class OrderSide(
    str,
    Enum,
):
    """
    Direção da ordem.

    BUY  -> compra
    SELL -> venda
    """

    BUY = "BUY"

    SELL = "SELL"
