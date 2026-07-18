from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.orders import OrderId
from app.domain.common.financial_core.orders.entities import Order
from app.domain.common.financial_core.orders.enums import OrderSide
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.value_objects.money import Money


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def test_create_order():

    order = Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.BUY,
        quantity=Decimal("10"),
        price=Money("30.00", BRL),
    )

    assert order.asset.symbol == "PETR4"

    assert order.side == OrderSide.BUY


def test_notional():

    order = Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.BUY,
        quantity=Decimal("10"),
        price=Money("30.00", BRL),
    )

    assert order.notional.value == Decimal("300.00")


def test_buy_property():

    order = Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.BUY,
        quantity=Decimal("10"),
        price=Money("30.00", BRL),
    )

    assert order.is_buy is True


def test_sell_property():

    order = Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.SELL,
        quantity=Decimal("10"),
        price=Money("30.00", BRL),
    )

    assert order.is_sell is True


def test_quantity_validation():

    with pytest.raises(
        ValueError,
    ):

        Order(
            order_id=OrderId.new(),
            asset=Asset("PETR4"),
            side=OrderSide.BUY,
            quantity=Decimal("0"),
            price=Money("30.00", BRL),
        )
