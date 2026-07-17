from decimal import Decimal

from app.domain.common.financial_core.currency.currency import (
    Currency,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.portfolio.positions.position import (
    Position,
)

from app.domain.common.financial_core.portfolio.portfolio import (
    Portfolio,
)

from app.domain.common.financial_core.portfolio.performance import (
    PortfolioPerformance,
)


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def create_position():

    return Position(
        asset=Asset("PETR4"),
        quantity=Decimal("10"),
        average_price=Money(
            "30.00",
            BRL,
        ),
    )


def test_invested_capital():

    portfolio = Portfolio("Carteira")

    portfolio.add_position(
        create_position(),
    )

    performance = PortfolioPerformance(
        portfolio,
    )

    assert (
        performance.invested_capital().value
        == Decimal("300.00")
    )


def test_market_value():

    portfolio = Portfolio("Carteira")

    portfolio.add_position(
        create_position(),
    )

    performance = PortfolioPerformance(
        portfolio,
    )

    prices = {
        "PETR4": Money(
            "40.00",
            BRL,
        )
    }

    assert (
        performance.market_value(
            prices,
        ).value
        == Decimal("400.00")
    )


def test_profit_loss():

    portfolio = Portfolio("Carteira")

    portfolio.add_position(
        create_position(),
    )

    performance = PortfolioPerformance(
        portfolio,
    )

    prices = {
        "PETR4": Money(
            "40.00",
            BRL,
        )
    }

    assert (
        performance.profit_loss(
            prices,
        ).value
        == Decimal("100.00")
    )


def test_return_percentage():

    portfolio = Portfolio("Carteira")

    portfolio.add_position(
        create_position(),
    )

    performance = PortfolioPerformance(
        portfolio,
    )

    prices = {
        "PETR4": Money(
            "45.00",
            BRL,
        )
    }

    assert (
        performance.return_percentage(
            prices,
        )
        == Decimal("0.5")
    )


def test_is_profitable():

    portfolio = Portfolio("Carteira")

    portfolio.add_position(
        create_position(),
    )

    performance = PortfolioPerformance(
        portfolio,
    )

    prices = {
        "PETR4": Money(
            "50.00",
            BRL,
        )
    }

    assert performance.is_profitable(
        prices,
    )


def test_is_loss():

    portfolio = Portfolio("Carteira")

    portfolio.add_position(
        create_position(),
    )

    performance = PortfolioPerformance(
        portfolio,
    )

    prices = {
        "PETR4": Money(
            "20.00",
            BRL,
        )
    }

    assert performance.is_loss(
        prices,
    )
