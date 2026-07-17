from decimal import Decimal

import pytest

from app.domain.common.financial_core.allocation.models import (
    AllocationResult,
)
from app.domain.common.financial_core.currency.currency import (
    Currency,
)
from app.domain.common.financial_core.value_objects.money import (
    Money,
)


BRL = Currency(
    "BRL",
    "R$",
    "Real Brasileiro",
)


def test_allocation_result_creation():

    amount = Money(
        "500.00",
        BRL,
    )

    result = AllocationResult(
        target="PETR4",
        amount=amount,
        weight=Decimal("50"),
    )

    assert result.target == "PETR4"
    assert result.amount == amount
    assert result.weight == Decimal("50")


def test_allocation_result_is_immutable():

    amount = Money(
        "500.00",
        BRL,
    )

    result = AllocationResult(
        target="PETR4",
        amount=amount,
        weight=Decimal("50"),
    )

    with pytest.raises(
        AttributeError
    ):

        result.weight = Decimal("60")


def test_negative_weight_not_allowed():

    amount = Money(
        "500.00",
        BRL,
    )

    with pytest.raises(
        ValueError
    ):

        AllocationResult(
            target="PETR4",
            amount=amount,
            weight=Decimal("-1"),
        )


def test_weight_above_100_not_allowed():

    amount = Money(
        "500.00",
        BRL,
    )

    with pytest.raises(
        ValueError
    ):

        AllocationResult(
            target="PETR4",
            amount=amount,
            weight=Decimal("101"),
        )
