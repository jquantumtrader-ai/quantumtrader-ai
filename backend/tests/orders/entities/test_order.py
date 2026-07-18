from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.orders import OrderId
from app.domain.common.financial_core.orders.entities import Order
from app.domain.common.financial_core.orders.enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.value_objects.money import Money


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def create_order(
    status: OrderStatus = OrderStatus.CREATED,
) -> Order:

    return Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        status=status,
        quantity=Decimal("10"),
        price=Money("30.00", BRL),
    )


def test_create_order():

    order = create_order()

    assert (
        order.status
        ==
        OrderStatus.CREATED
    )


def test_notional():

    order = create_order()

    assert (
        order.notional.value
        ==
        Decimal("300.00")
    )


def test_filled_status():

    order = create_order(
        OrderStatus.FILLED,
    )

    assert order.is_filled is True


def test_cancelled_status():

    order = create_order(
        OrderStatus.CANCELLED,
    )

    assert order.is_cancelled is True


def test_rejected_status():

    order = create_order(
        OrderStatus.REJECTED,
    )

    assert order.is_rejected is True


def test_quantity_validation():

    with pytest.raises(
        ValueError,
    ):

        Order(
            order_id=OrderId.new(),
            asset=Asset("PETR4"),
            side=OrderSide.BUY,
            order_type=OrderType.MARKET,
            status=OrderStatus.CREATED,
            quantity=Decimal("0"),
            price=Money("30.00", BRL),
        )
