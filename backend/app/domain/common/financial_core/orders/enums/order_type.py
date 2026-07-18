from __future__ import annotations

from enum import Enum


class OrderType(
    str,
    Enum,
):
    """
    Tipo de execução da ordem.

    MARKET:
        Executa imediatamente pelo preço disponível.

    LIMIT:
        Executa somente no preço determinado.

    STOP:
        Ativa quando o preço de gatilho é atingido.

    STOP_LIMIT:
        Ativa uma ordem limitada após o gatilho.
    """

    MARKET = "MARKET"

    LIMIT = "LIMIT"

    STOP = "STOP"

    STOP_LIMIT = "STOP_LIMIT"
