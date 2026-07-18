from decimal import Decimal

import pytest

from app.domain.common.financial_core.orders import OrderId
from app.domain.common.financial_core.orders.fills import Fill
from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.value_objects.money import Money



BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)



def test_create_fill():

    fill = Fill(
        order_id=OrderId.new(),
        quantity=Decimal("10"),
        price=Money(
            "30.00",
            BRL,
        ),
    )


    assert (
        fill.quantity
        ==
        Decimal("10")
    )



def test_fill_value():

    fill = Fill(
        order_id=OrderId.new(),
        quantity=Decimal("10"),
        price=Money(
            "30.00",
            BRL,
        ),
    )


    assert (
        fill.value.value
        ==
        Decimal("300.00")
    )



def test_negative_fill_quantity():

    with pytest.raises(
        ValueError,
    ):

        Fill(
            order_id=OrderId.new(),
            quantity=Decimal("-1"),
            price=Money(
                "30.00",
                BRL,
            ),
        )
