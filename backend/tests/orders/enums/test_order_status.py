from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)


def test_order_status_values():

    assert (
        OrderStatus.CREATED.value
        ==
        "CREATED"
    )

    assert (
        OrderStatus.SUBMITTED.value
        ==
        "SUBMITTED"
    )

    assert (
        OrderStatus.PARTIALLY_FILLED.value
        ==
        "PARTIALLY_FILLED"
    )

    assert (
        OrderStatus.FILLED.value
        ==
        "FILLED"
    )

    assert (
        OrderStatus.CANCELLED.value
        ==
        "CANCELLED"
    )

    assert (
        OrderStatus.REJECTED.value
        ==
        "REJECTED"
    )
