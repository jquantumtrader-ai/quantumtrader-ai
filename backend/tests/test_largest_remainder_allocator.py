from decimal import Decimal

import pytest

from app.domain.common.financial_core.currency.predefined import (
    BRL,
)
from app.domain.common.financial_core.allocation import (
    LargestRemainderAllocator,
)
from app.domain.common.financial_core.value_objects.money import (
    Money,
)
from app.domain.common.financial_core.allocation.exceptions import (
    EmptyAllocationError,
    InvalidAllocationRatioError,
)


def test_basic_allocation() -> None:

    allocator = LargestRemainderAllocator()

    money = Money(
        "100",
        BRL,
    )

    result = allocator.allocate(
        money,
        [1, 1, 1],
    )

    total = sum(
        item.value
        for item in result
    )

    assert total == Decimal("100")


def test_allocation_preserves_currency() -> None:

    allocator = LargestRemainderAllocator()

    money = Money(
        "500",
        BRL,
    )

    result = allocator.allocate(
        money,
        [2, 3],
    )

    assert all(
        item.currency == BRL
        for item in result
    )


def test_stable_order_when_equal_remainder() -> None:

    allocator = LargestRemainderAllocator()

    money = Money(
        "100.00000001",
        BRL,
    )

    result = allocator.allocate(
        money,
        [1, 1, 1],
    )

    assert (
        result[0].value
        >= result[1].value
    )


def test_empty_ratios_error() -> None:

    allocator = LargestRemainderAllocator()

    with pytest.raises(
        EmptyAllocationError
    ):

        allocator.allocate(
            Money("100", BRL),
            [],
        )


def test_negative_ratio_error() -> None:

    allocator = LargestRemainderAllocator()

    with pytest.raises(
        InvalidAllocationRatioError
    ):

        allocator.allocate(
            Money("100", BRL),
            [1, -1],
        )


def test_large_allocation() -> None:

    allocator = LargestRemainderAllocator()

    money = Money(
        "1000000",
        BRL,
    )

    result = allocator.allocate(
        money,
        [1, 2, 3, 4],
    )

    total = sum(
        item.value
        for item in result
    )

    assert total == Decimal(
        "1000000"
    )
