from decimal import Decimal

from app.domain.common.financial_core.orders.execution_report import (
    OrderExecutionReport,
)

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)

from app.domain.common.financial_core.orders.fills import (
    Fill,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)

from app.domain.common.financial_core.currency.currency import (
    Currency,
)


from tests.orders.fills.test_order_fill_tracking import (
    create_order,
)


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)



def test_execution_report():

    order = create_order()


    order = order.add_fill(
        Fill(
            order_id=order.order_id,
            quantity=Decimal("40"),
            price=Money(
                "30",
                BRL,
            ),
        )
    )


    report = (
        OrderExecutionReport
        .from_order(order)
    )


    assert (
        report.asset_symbol
        ==
        "PETR4"
    )


    assert (
        report.requested_quantity
        ==
        Decimal("100")
    )


    assert (
        report.executed_quantity
        ==
        Decimal("40")
    )


    assert (
        report.remaining_quantity
        ==
        Decimal("60")
    )


    assert (
        report.fills_count
        ==
        1
    )



def test_average_execution_price_report():

    order = create_order()


    order = order.add_fill(
        Fill(
            order_id=order.order_id,
            quantity=Decimal("100"),
            price=Money(
                "32",
                BRL,
            ),
        )
    )


    report = (
        OrderExecutionReport
        .from_order(order)
    )


    assert (
        report.average_execution_price.value
        ==
        Decimal("32")
    )


    assert (
        report.executed_value.value
        ==
        Decimal("3200")
    )
