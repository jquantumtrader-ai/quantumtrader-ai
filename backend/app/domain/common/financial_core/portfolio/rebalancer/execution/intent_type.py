from enum import Enum


class IntentType(Enum):
    """
    Tipo de intenção de execução.
    """

    BUY = "BUY"

    SELL = "SELL"

    HOLD = "HOLD"
