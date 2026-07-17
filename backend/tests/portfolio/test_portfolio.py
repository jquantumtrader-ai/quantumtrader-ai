from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.currency import (
    Currency,
)

from app.domain.common.financial_core.portfolio.portfolio import (
    Portfolio,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.portfolio.positions.position import (
    Position,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def create_position(
    symbol: str,
    quantity: Decimal,
    price: str,
) -> Position:

    asset = Asset(
        symbol=symbol,
    )

    return Position(
        asset=asset,
        quantity=quantity,
        average_price=Money(
            price,
            BRL,
        ),
    )


def test_portfolio_creation():

    portfolio = Portfolio(
        name="Carteira Teste",
    )

    assert portfolio.name == "Carteira Teste"

    assert portfolio.positions == ()


def test_add_position():

    portfolio = Portfolio(
        name="Carteira Teste",
    )

    position = create_position(
        "PETR4",
        Decimal("10"),
        "30.00",
    )

    portfolio.add_position(
        position,
    )

    assert len(
        portfolio.positions,
    ) == 1

    assert (
        portfolio.positions[0]
        == position
    )


def test_total_cost():

    portfolio = Portfolio(
        name="Carteira Teste",
    )

    portfolio.add_position(
        create_position(
            "PETR4",
            Decimal("10"),
            "30.00",
        )
    )

    portfolio.add_position(
        create_position(
            "VALE3",
            Decimal("5"),
            "40.00",
        )
    )

    result = portfolio.total_cost()

    assert result.value == Decimal(
        "500.00",
    )

    assert result.currency == BRL


def test_market_value():

    portfolio = Portfolio(
        name="Carteira Teste",
    )

    portfolio.add_position(
        create_position(
            "PETR4",
            Decimal("10"),
            "30.00",
        )
    )

    prices = {
        "PETR4": Money(
            "35.00",
            BRL,
        ),
    }

    result = portfolio.market_value(
        prices,
    )

    assert result.value == Decimal(
        "350.00",
    )


def test_remove_position():

    portfolio = Portfolio(
        name="Carteira Teste",
    )

    portfolio.add_position(
        create_position(
            "PETR4",
            Decimal("10"),
            "30.00",
        )
    )

    portfolio.remove_position(
        "PETR4",
    )

    assert portfolio.positions == ()


def test_empty_portfolio_total_cost():

    portfolio = Portfolio(
        name="Carteira Teste",
    )

    with pytest.raises(
        ValueError,
    ):
        portfolio.total_cost()
