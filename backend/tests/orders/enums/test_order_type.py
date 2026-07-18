from app.domain.common.financial_core.orders.enums import (
    OrderType,
)


def test_order_type_values():

    assert (
        OrderType.MARKET.value
        ==
        "MARKET"
    )

    assert (
        OrderType.LIMIT.value
        ==
        "LIMIT"
    )

    assert (
        OrderType.STOP.value
        ==
        "STOP"
    )

    assert (
        OrderType.STOP_LIMIT.value
        ==
        "STOP_LIMIT"
    )


def test_order_type_is_string_enum():

    assert isinstance(
        OrderType.MARKET,
        str,
    )
