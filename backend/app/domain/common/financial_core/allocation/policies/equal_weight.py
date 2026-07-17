from __future__ import annotations

from decimal import Decimal

from ..largest_remainder_allocator import (
    LargestRemainderAllocator,
)

from ..models.allocation_request import (
    AllocationRequest,
)

from ..models.allocation_result import (
    AllocationResult,
)

from ..result_mapper import (
    map_to_allocation_results,
)

from ...value_objects.money import (
    Money,
)

from .base import (
    AllocationPolicy,
)


class EqualWeightAllocationPolicy(
    AllocationPolicy
):
    """
    Distribuição igualitária entre targets.
    """


    def __init__(
        self,
        allocator: LargestRemainderAllocator | None = None,
    ) -> None:

        self._allocator = (
            allocator
            or LargestRemainderAllocator()
        )


    def allocate(
        self,
        request: AllocationRequest,
    ) -> list[AllocationResult]:

        values: list[Money] = (
            self._allocator.allocate(
                request.amount,
                [
                    1
                    for _ in request.targets
                ],
            )
        )

        weight = (
            Decimal("100")
            /
            Decimal(
                len(request.targets)
            )
        )

        weights = [
            weight
            for _ in request.targets
        ]

        return map_to_allocation_results(
            request.targets,
            values,
            weights,
        )
