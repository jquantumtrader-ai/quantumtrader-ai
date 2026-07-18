from decimal import Decimal

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.portfolio.analytics import PortfolioAnalytics
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.portfolio.portfolio import Portfolio
from app.domain.common.financial_core.portfolio.positions.position import Position
from app.domain.common.financial_core.value_objects.money import Money


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def create_position(
    symbol: str,
    quantity: str,
    price: str,
) -> Position:

    return Position(
        asset=Asset(symbol),
        quantity=Decimal(quantity),
        average_price=Money(
            price,
            BRL,
        ),
    )


def create_prices():

    return {
        "PETR4": Money(
            "40.00",
            BRL,
        ),
        "VALE3": Money(
            "70.00",
            BRL,
        ),
    }


def create_portfolio():

    portfolio = Portfolio(
        "Carteira",
    )

    portfolio.add_position(
        create_position(
            "PETR4",
            "10",
            "30.00",
        )
    )

    portfolio.add_position(
        create_position(
            "VALE3",
            "5",
            "70.00",
        )
    )

    return portfolio


def test_total_market_value():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    assert (
        analytics.total_market_value(
            create_prices(),
        ).value
        == Decimal("750.00")
    )


def test_weights_sum_to_one():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    weights = analytics.weights(
        create_prices(),
    )

    total = sum(
        weights.values(),
    )

    assert total == Decimal("1")


def test_largest_position():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    assert (
        analytics.largest_position(
            create_prices(),
        )
        == "PETR4"
    )


def test_smallest_position():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    assert (
        analytics.smallest_position(
            create_prices(),
        )
        == "VALE3"
    )


def test_concentration():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    concentration = analytics.concentration(
        create_prices(),
    )

    assert concentration == Decimal(
        "0.5333333333333333333333333333"
    )


def test_not_concentrated():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    assert (
        analytics.is_concentrated(
            create_prices(),
            limit=Decimal("0.60"),
        )
        is False
    )


def test_diversification_index():

    analytics = PortfolioAnalytics(
        create_portfolio(),
    )

    value = analytics.diversification_index(
        create_prices(),
    )

    assert value > Decimal("0")
