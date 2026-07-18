from decimal import Decimal

from app.domain.common.financial_core.currency.currency import Currency
from app.domain.common.financial_core.portfolio.assets.asset import Asset
from app.domain.common.financial_core.portfolio.rebalancer.rebalance_action import (
    RebalanceAction,
)
from app.domain.common.financial_core.portfolio.rebalancer.rebalance_plan import (
    RebalancePlan,
)
from app.domain.common.financial_core.portfolio.rebalancer.report.rebalance_report import (
    RebalanceReport,
)
from app.domain.common.financial_core.value_objects.money import Money


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def test_build_report():

    asset = Asset(
        "PETR4",
    )

    action = RebalanceAction(
        asset=asset,
        current_quantity=Decimal("10"),
        target_quantity=Decimal("12"),
        quantity_difference=Decimal("2"),
        current_weight=Decimal("0.40"),
        target_weight=Decimal("0.50"),
        current_value=Money("100", BRL),
        target_value=Money("120", BRL),
        value_difference=Money("20", BRL),
    )

    plan = RebalancePlan(
        actions=[action],
    )

    report = RebalanceReport(
        plan,
    )

    assert report.total_orders == 1
    assert report.total_buy_orders == 1
    assert report.total_sell_orders == 0
    assert report.total_hold_orders == 0
