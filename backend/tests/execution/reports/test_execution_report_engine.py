from decimal import Decimal

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)

from app.domain.common.financial_core.execution.reports import (
    ExecutionReportEngine,
)



def test_generate_partial_report():

    engine = ExecutionReportEngine()

    report = engine.generate(
        fills=[
            (
                Decimal("40"),
                Decimal("30"),
            ),
        ],
        requested_quantity=Decimal(
            "100",
        ),
    )

    assert report.total_quantity == Decimal(
        "40",
    )

    assert report.average_price == Decimal(
        "30",
    )

    assert report.status == ExecutionStatus.PARTIAL

    assert report.completed is False



def test_generate_filled_report():

    engine = ExecutionReportEngine()

    report = engine.generate(
        fills=[
            (
                Decimal("50"),
                Decimal("30"),
            ),
            (
                Decimal("50"),
                Decimal("32"),
            ),
        ],
        requested_quantity=Decimal(
            "100",
        ),
    )

    assert report.total_quantity == Decimal(
        "100",
    )

    assert report.average_price == Decimal(
        "31",
    )

    assert report.status == ExecutionStatus.FILLED

    assert report.completed is True
