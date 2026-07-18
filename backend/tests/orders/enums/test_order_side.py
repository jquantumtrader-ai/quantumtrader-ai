from app.domain.common.financial_core.orders.enums import (
    OrderSide,
)


def test_order_side_values():

    assert (
        OrderSide.BUY.value
        ==
        "BUY"
    )

    assert (
        OrderSide.SELL.value
        ==
        "SELL"
    )


def test_order_side_is_string_enum():

    assert isinstance(
        OrderSide.BUY,
        str,
    )
