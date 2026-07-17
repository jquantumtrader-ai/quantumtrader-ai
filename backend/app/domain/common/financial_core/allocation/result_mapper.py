from __future__ import annotations

from decimal import Decimal
from typing import Sequence

from .models.allocation_result import (
    AllocationResult,
)

from ..value_objects.money import Money


def map_to_allocation_results(
    targets: Sequence[object],
    amounts: Sequence[Money],
    weights: Sequence[Decimal],
) -> list[AllocationResult]:
    """
    Converte valores alocados em resultados de domínio.
    """

    if not (
        len(targets)
        == len(amounts)
        == len(weights)
    ):
        raise ValueError(
            "Targets, amounts e weights devem possuir o mesmo tamanho."
        )


    return [
        AllocationResult(
            target=target,
            amount=amount,
            weight=weight,
        )
        for target, amount, weight in zip(
            targets,
            amounts,
            weights,
        )
    ]
