from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.orders import OrderId
from app.domain.common.financial_core.orders.entities import Order
from app.domain.common.financial_core.orders.enums import (
    OrderSide,
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
    side: OrderSide = OrderSide.BUY,
    order_type: OrderType = OrderType.MARKET,
) -> Order:

    return Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=side,
        order_type=order_type,
        quantity=Decimal("10"),
        price=Money("30.00", BRL),
    )


def test_create_order():

    order = create_order()

    assert order.asset.symbol == "PETR4"

    assert order.side == OrderSide.BUY

    assert order.order_type == OrderType.MARKET


def test_notional():

    order = create_order()

    assert (
        order.notional.value
        ==
        Decimal("300.00")
    )


def test_buy_property():

    order = create_order(
        side=OrderSide.BUY,
    )

    assert order.is_buy is True

    assert order.is_sell is False


def test_sell_property():

    order = create_order(
        side=OrderSide.SELL,
    )

    assert order.is_sell is True

    assert order.is_buy is False


def test_market_order():

    order = create_order(
        order_type=OrderType.MARKET,
    )

    assert (
        order.order_type
        ==
        OrderType.MARKET
    )


def test_limit_order():

    order = create_order(
        order_type=OrderType.LIMIT,
    )

    assert (
        order.order_type
        ==
        OrderType.LIMIT
    )


def test_stop_order():

    order = create_order(
        order_type=OrderType.STOP,
    )

    assert (
        order.order_type
        ==
        OrderType.STOP
    )


def test_stop_limit_order():

    order = create_order(
        order_type=OrderType.STOP_LIMIT,
    )

    assert (
        order.order_type
        ==
        OrderType.STOP_LIMIT
    )


def test_quantity_validation():

    with pytest.raises(
        ValueError,
    ):

        Order(
            order_id=OrderId.new(),
            asset=Asset("PETR4"),
            side=OrderSide.BUY,
            order_type=OrderType.MARKET,
            quantity=Decimal("0"),
            price=Money("30.00", BRL),
        )
