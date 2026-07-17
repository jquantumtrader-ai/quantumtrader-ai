from decimal import Decimal

from app.domain.common.financial_core.currency.currency import (
    Currency,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
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

from app.domain.common.financial_core.portfolio.metrics.portfolio_metrics import (
    PortfolioMetrics,
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

    return Position(
        asset=Asset(symbol),
        quantity=quantity,
        average_price=Money(
            price,
            BRL,
        ),
    )


def test_unrealized_pnl():

    portfolio = Portfolio(
        name="Teste",
    )

    portfolio.add_position(
        create_position(
            "PETR4",
            Decimal("10"),
            "30.00",
        )
    )

    metrics = PortfolioMetrics(
        portfolio,
    )

    result = metrics.unrealized_pnl(
        {
            "PETR4": Money(
                "35.00",
                BRL,
            )
        }
    )

    assert result.value == Decimal(
        "50.00"
    )


def test_allocation_weights():

    portfolio = Portfolio(
        name="Teste",
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


    metrics = PortfolioMetrics(
        portfolio,
    )


    weights = metrics.allocation_weights(
        {
            "PETR4": Money(
                "40.00",
                BRL,
            ),
            "VALE3": Money(
                "40.00",
                BRL,
            ),
        }
    )


    assert weights["PETR4"] == Decimal(
        "0.6666666666666666666666666667"
    )

    assert weights["VALE3"] == Decimal(
        "0.3333333333333333333333333333"
    )
