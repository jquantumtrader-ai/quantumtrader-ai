from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.portfolio import Portfolio
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.portfolio.positions.position import Position
from app.domain.common.financial_core.portfolio.rebalancer.validator import (
    PortfolioRebalanceValidator,
)
from app.domain.common.financial_core.value_objects.money import Money

BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def create_portfolio() -> Portfolio:

    portfolio = Portfolio(
        name="Carteira",
    )

    portfolio.add_position(
        Position(
            asset=Asset("PETR4"),
            quantity=Decimal("10"),
            average_price=Money(
                "30",
                BRL,
            ),
        )
    )

    portfolio.add_position(
        Position(
            asset=Asset("VALE3"),
            quantity=Decimal("5"),
            average_price=Money(
                "50",
                BRL,
            ),
        )
    )

    return portfolio


def create_prices():

    return {
        "PETR4": Money(
            "40",
            BRL,
        ),
        "VALE3": Money(
            "70",
            BRL,
        ),
    }


def test_validator_accepts_valid_data():

    validator = PortfolioRebalanceValidator()

    validator.validate(
        create_portfolio(),
        create_prices(),
        {
            "PETR4": Decimal("0.5"),
            "VALE3": Decimal("0.5"),
        },
    )


def test_validator_requires_total_weight():

    validator = PortfolioRebalanceValidator()

    with pytest.raises(ValueError):

        validator.validate(
            create_portfolio(),
            create_prices(),
            {
                "PETR4": Decimal("0.4"),
                "VALE3": Decimal("0.4"),
            },
        )


def test_validator_negative_weight():

    validator = PortfolioRebalanceValidator()

    with pytest.raises(ValueError):

        validator.validate(
            create_portfolio(),
            create_prices(),
            {
                "PETR4": Decimal("-0.2"),
                "VALE3": Decimal("1.2"),
            },
        )


def test_validator_requires_prices():

    validator = PortfolioRebalanceValidator()

    with pytest.raises(ValueError):

        validator.validate(
            create_portfolio(),
            {
                "PETR4": Money(
                    "40",
                    BRL,
                )
            },
            {
                "PETR4": Decimal("0.5"),
                "VALE3": Decimal("0.5"),
            },
        )


def test_validator_invalid_price():

    validator = PortfolioRebalanceValidator()

    with pytest.raises(ValueError):

        validator.validate(
            create_portfolio(),
            {
                "PETR4": Money(
                    "0",
                    BRL,
                ),
                "VALE3": Money(
                    "70",
                    BRL,
                ),
            },
            {
                "PETR4": Decimal("0.5"),
                "VALE3": Decimal("0.5"),
            },
        )
