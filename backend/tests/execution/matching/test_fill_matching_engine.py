from decimal import Decimal

import pytest

from app.domain.common.financial_core.execution.matching import (
    FillMatchingEngine,
)


def test_partial_fill():

    engine = FillMatchingEngine()

    result = engine.match(
        requested_quantity=Decimal(
            "100",
        ),
        current_filled_quantity=Decimal(
            "0",
        ),
        fill_quantity=Decimal(
            "40",
        ),
    )

    assert result.filled_quantity == Decimal(
        "40",
    )

    assert result.remaining_quantity == Decimal(
        "60",
    )

    assert result.completed is False



def test_complete_fill():

    engine = FillMatchingEngine()

    result = engine.match(
        requested_quantity=Decimal(
            "100",
        ),
        current_filled_quantity=Decimal(
            "40",
        ),
        fill_quantity=Decimal(
            "60",
        ),
    )

    assert result.filled_quantity == Decimal(
        "100",
    )

    assert result.remaining_quantity == Decimal(
        "0",
    )

    assert result.completed is True



def test_fill_overflow():

    engine = FillMatchingEngine()

    with pytest.raises(
        ValueError,
    ):

        engine.match(
            requested_quantity=Decimal(
                "100",
            ),
            current_filled_quantity=Decimal(
                "90",
            ),
            fill_quantity=Decimal(
                "20",
            ),
        )
