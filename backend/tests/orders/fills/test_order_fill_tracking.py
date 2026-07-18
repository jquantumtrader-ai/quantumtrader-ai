from decimal import Decimal

from app.domain.common.financial_core.orders import OrderId
from app.domain.common.financial_core.orders.entities import Order
from app.domain.common.financial_core.orders.enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.domain.common.financial_core.orders.fills import Fill
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.value_objects.money import Money



BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)



def create_order():

    return Order(
        order_id=OrderId.new(),
        asset=Asset("PETR4"),
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        status=OrderStatus.SUBMITTED,
        quantity=Decimal("100"),
        price=Money(
            "30",
            BRL,
        ),
    )



def test_add_partial_fill():

    order = create_order()

    fill = Fill(
        order_id=order.order_id,
        quantity=Decimal("40"),
        price=Money(
            "30",
            BRL,
        ),
    )


    updated = order.add_fill(
        fill,
    )


    assert (
        updated.executed_quantity
        ==
        Decimal("40")
    )


    assert (
        updated.remaining_quantity
        ==
        Decimal("60")
    )


    assert (
        updated.status
        ==
        OrderStatus.PARTIALLY_FILLED
    )



def test_average_execution_price():

    order = create_order()


    order = order.add_fill(
        Fill(
            order_id=order.order_id,
            quantity=Decimal("50"),
            price=Money(
                "30",
                BRL,
            ),
        )
    )


    order = order.add_fill(
        Fill(
            order_id=order.order_id,
            quantity=Decimal("50"),
            price=Money(
                "32",
                BRL,
            ),
        )
    )


    assert (
        order.average_execution_price.value
        ==
        Decimal("31")
    )
