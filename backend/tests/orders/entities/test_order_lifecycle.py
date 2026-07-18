from decimal import Decimal

import pytest

from app.domain.common.financial_core.orders import OrderId
from app.domain.common.financial_core.orders.entities import Order
from app.domain.common.financial_core.orders.enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.domain.common.financial_core.orders.state import (
    InvalidOrderTransition,
)
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.value_objects.money import Money


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)



def create_order() -> Order:

    return Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        status=OrderStatus.CREATED,
        quantity=Decimal("10"),
        price=Money(
            "30.00",
            BRL,
        ),
    )



def test_submit_order():

    order = create_order()

    submitted = order.submit()

    assert (
        submitted.status
        ==
        OrderStatus.SUBMITTED
    )



def test_fill_order():

    order = (
        create_order()
        .submit()
    )

    filled = order.fill()

    assert (
        filled.status
        ==
        OrderStatus.FILLED
    )



def test_cancel_order():

    order = create_order()

    cancelled = order.cancel()

    assert (
        cancelled.status
        ==
        OrderStatus.CANCELLED
    )



def test_partial_fill():

    order = (
        create_order()
        .submit()
    )

    partial = order.partially_fill()

    assert (
        partial.status
        ==
        OrderStatus.PARTIALLY_FILLED
    )



def test_invalid_transition():

    order = (
        create_order()
        .submit()
        .fill()
    )

    with pytest.raises(
        InvalidOrderTransition,
    ):

        order.submit()
