from decimal import (
    Decimal,
    Context,
    ROUND_HALF_EVEN,
    setcontext,
)


FINANCIAL_CONTEXT = Context(
    prec=28,
    rounding=ROUND_HALF_EVEN,
)


setcontext(FINANCIAL_CONTEXT)


def to_decimal(value) -> Decimal:
    """
    Conversão segura para Decimal.

    O Financial Core não aceita float.
    """

    if isinstance(value, float):
        raise TypeError(
            "Float não é permitido no Financial Core. "
            "Use string ou Decimal."
        )

    return Decimal(value)
