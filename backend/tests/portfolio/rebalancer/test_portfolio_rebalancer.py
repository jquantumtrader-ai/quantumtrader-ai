from decimal import Decimal

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.portfolio.portfolio import Portfolio
from app.domain.common.financial_core.portfolio.positions.position import Position
from app.domain.common.financial_core.portfolio.rebalancer import PortfolioRebalancer
from app.domain.common.financial_core.value_objects.money import Money


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def create_position(
    symbol,
    quantity,
    price,
):

    return Position(
        asset=Asset(symbol),
        quantity=Decimal(quantity),
        average_price=Money(
            price,
            BRL,
        ),
    )


def create_portfolio():

    portfolio = Portfolio(
        "Carteira",
    )

    portfolio.add_position(
        create_position(
            "PETR4",
            "10",
            "30",
        )
    )

    portfolio.add_position(
        create_position(
            "VALE3",
            "5",
            "70",
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


def test_rebalance_plan():

    reb = PortfolioRebalancer(
        create_portfolio(),
    )

    plan = reb.rebalance(

        create_prices(),

        {

            "PETR4": Decimal(
                "0.50"
            ),

            "VALE3": Decimal(
                "0.50"
            ),

        },

    )

    assert len(
        plan.actions
    ) == 2


def test_current_weight():

    reb = PortfolioRebalancer(
        create_portfolio(),
    )

    plan = reb.rebalance(

        create_prices(),

        {

            "PETR4": Decimal(
                "0.50"
            ),

            "VALE3": Decimal(
                "0.50"
            ),

        },

    )

    assert (
        plan.actions[
            0
        ].current_weight
        > Decimal("0")
    )


def test_target_weight():

    reb = PortfolioRebalancer(
        create_portfolio(),
    )

    plan = reb.rebalance(

        create_prices(),

        {

            "PETR4": Decimal(
                "0.50"
            ),

            "VALE3": Decimal(
                "0.50"
            ),

        },

    )

    assert (
        plan.actions[
            0
        ].target_weight
        == Decimal("0.50")
    )
def test_quantity_difference():

    rebalancer = PortfolioRebalancer(
        create_portfolio(),
    )

    plan = rebalancer.rebalance(
        create_prices(),
        {
            "PETR4": Decimal(
                "0.50"
            ),
            "VALE3": Decimal(
                "0.50"
            ),
        },
    )

    petr = plan.actions[0]

    assert (
        petr.target_quantity
        <
        petr.current_quantity
    )

    assert (
        petr.quantity_difference
        <
        Decimal("0")
    )
