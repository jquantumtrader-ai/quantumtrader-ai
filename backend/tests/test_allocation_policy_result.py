from decimal import Decimal

from app.domain.common.financial_core.allocation.models import (
    AllocationRequest,
    AllocationResult,
)

from app.domain.common.financial_core.allocation.policies import (
    EqualWeightAllocationPolicy,
    PercentageAllocationPolicy,
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


def test_equal_weight_returns_allocation_result():

    policy = EqualWeightAllocationPolicy()

    request = AllocationRequest(
        amount=Money(
            "100.00",
            BRL,
        ),
        targets=[
            "PETR4",
            "VALE3",
        ],
    )

    result = policy.allocate(
        request,
    )

    assert isinstance(
        result[0],
        AllocationResult,
    )

    assert result[0].target == "PETR4"

    assert result[0].amount.currency == BRL



def test_percentage_returns_allocation_result():

    policy = PercentageAllocationPolicy()

    request = AllocationRequest(
        amount=Money(
            "1000.00",
            BRL,
        ),
        targets=[
            "PETR4",
            "VALE3",
        ],
        weights=[
            Decimal("70"),
            Decimal("30"),
        ],
    )

    result = policy.allocate(
        request,
    )

    assert isinstance(
        result[0],
        AllocationResult,
    )

    assert result[0].target == "PETR4"

    assert result[0].weight == Decimal("70")



def test_allocation_result_preserves_total():

    policy = EqualWeightAllocationPolicy()

    request = AllocationRequest(
        amount=Money(
            "100.00",
            BRL,
        ),
        targets=[
            "A",
            "B",
            "C",
        ],
    )

    result = policy.allocate(
        request,
    )

    total = sum(
        item.amount.value
        for item in result
    )

    assert total == Decimal(
        "100.00"
    )
