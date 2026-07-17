from decimal import Decimal

from app.domain.common.financial_core.allocation.models import (
    AllocationRequest,
)

from app.domain.common.financial_core.allocation.policies import (
    EqualWeightAllocationPolicy,
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


def test_equal_weight_allocation():

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

    values = [
        item.value
        for item in result
    ]

    assert values == [
        Decimal("33.34"),
        Decimal("33.33"),
        Decimal("33.33"),
    ]


def test_equal_weight_preserves_currency():

    policy = EqualWeightAllocationPolicy()

    request = AllocationRequest(
        amount=Money(
            "50.00",
            BRL,
        ),
        targets=[
            "A",
            "B",
        ],
    )

    result = policy.allocate(
        request,
    )

    assert all(
        item.currency == BRL
        for item in result
    )


def test_equal_weight_distribution():

    policy = EqualWeightAllocationPolicy()

    request = AllocationRequest(
        amount=Money(
            "10.00",
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

    values = [
        item.value
        for item in result
    ]

    assert values == [
        Decimal("3.34"),
        Decimal("3.33"),
        Decimal("3.33"),
    ]
