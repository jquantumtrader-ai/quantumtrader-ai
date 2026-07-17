from __future__ import annotations

from decimal import Decimal

from .models.allocation_result import (
    AllocationResult,
)

from ..value_objects.money import (
    Money,
)


def map_to_allocation_results(
    targets: list[object],
    values: list[Money],
    weights: list[Decimal],
) -> list[AllocationResult]:
    """
    Converte valores monetários em resultados
    completos de alocação.
    """

    return [
        AllocationResult(
            target=target,
            amount=value,
            weight=weight,
        )
        for target, value, weight
        in zip(
            targets,
            values,
            weights,
        )
    ]
