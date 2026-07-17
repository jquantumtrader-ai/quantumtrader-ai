from decimal import Decimal

import pytest

from app.domain.common.financial_core.allocation.models import (
    AllocationRequest,
)

from app.domain.common.financial_core.allocation.policies import (
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


def test_percentage_allocation():

    policy = PercentageAllocationPolicy()

    amount = Money(
        "1000.00",
        BRL,
    )

    request = AllocationRequest(
        amount=amount,
        targets=[
            "A",
            "B",
            "C",
        ],
        weights=[
            Decimal("50"),
            Decimal("30"),
            Decimal("20"),
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
        Decimal("500.00"),
        Decimal("300.00"),
        Decimal("200.00"),
    ]


def test_percentage_preserves_total():

    policy = PercentageAllocationPolicy()

    amount = Money(
        "100.00",
        BRL,
    )

    request = AllocationRequest(
        amount=amount,
        targets=[
            "A",
            "B",
            "C",
        ],
        weights=[
            Decimal("33"),
            Decimal("33"),
            Decimal("34"),
        ],
    )

    result = policy.allocate(
        request,
    )

    assert sum(
        item.value
        for item in result
    ) == Decimal("100.00")


def test_percentage_requires_100_total():

    policy = PercentageAllocationPolicy()

    amount = Money(
        "100.00",
        BRL,
    )

    request = AllocationRequest(
        amount=amount,
        targets=[
            "A",
            "B",
        ],
        weights=[
            Decimal("50"),
            Decimal("20"),
        ],
    )

    with pytest.raises(
        ValueError,
    ):

        policy.allocate(
            request,
        )


def test_percentage_requires_same_length():

    amount = Money(
        "100.00",
        BRL,
    )

    with pytest.raises(
        ValueError,
    ):

        AllocationRequest(
            amount=amount,
            targets=[
                "A",
                "B",
                "C",
            ],
            weights=[
                Decimal("50"),
                Decimal("50"),
            ],
        )


def test_percentage_requires_weights():

    policy = PercentageAllocationPolicy()

    amount = Money(
        "100.00",
        BRL,
    )

    request = AllocationRequest(
        amount=amount,
        targets=[
            "A",
            "B",
        ],
    )

    with pytest.raises(
        ValueError,
    ):

        policy.allocate(
            request,
        )
