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


class PercentageAllocationPolicy(
    AllocationPolicy
):
    """
    Política baseada em percentuais.
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

        if request.weights is None:
            raise ValueError(
                "Percentuais são obrigatórios."
            )


        total = sum(
            Decimal(weight)
            for weight in request.weights
        )


        if total != Decimal("100"):
            raise ValueError(
                "A soma dos percentuais deve ser 100."
            )


        ratios = [
            int(weight)
            for weight in request.weights
        ]


        values: list[Money] = (
            self._allocator.allocate(
                request.amount,
                ratios,
            )
        )


        weights = [
            Decimal(weight)
            for weight in request.weights
        ]


        return map_to_allocation_results(
            request.targets,
            values,
            weights,
        )
