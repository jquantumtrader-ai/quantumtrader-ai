from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.currency import (
    Currency,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)

from app.domain.common.financial_core.portfolio.assets import (
    Asset,
)

from app.domain.common.financial_core.portfolio.positions import (
    Position,
)


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def test_position_creation():

    position = Position(
        asset=Asset("petr4"),
        quantity=Decimal("100"),
        average_price=Money(
            "35.50",
            BRL,
        ),
    )

    assert position.asset.symbol == "PETR4"
    assert position.quantity == Decimal("100")



def test_position_cost_basis():

    position = Position(
        asset=Asset("PETR4"),
        quantity=Decimal("100"),
        average_price=Money(
            "35.50",
            BRL,
        ),
    )

    assert (
        position.cost_basis.value
        == Decimal("3550.00")
    )



def test_position_market_value():

    position = Position(
        asset=Asset("PETR4"),
        quantity=Decimal("100"),
        average_price=Money(
            "35.50",
            BRL,
        ),
    )


    result = position.market_value(
        Money(
            "40.00",
            BRL,
        )
    )


    assert result.value == Decimal(
        "4000.00"
    )



def test_position_invalid_quantity():

    with pytest.raises(ValueError):

        Position(
            asset=Asset("PETR4"),
            quantity=Decimal("0"),
            average_price=Money(
                "35.50",
                BRL,
            ),
        )
