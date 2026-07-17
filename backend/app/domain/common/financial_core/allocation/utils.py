from __future__ import annotations

from .exceptions import (
    EmptyAllocationError,
    InvalidAllocationRatioError,
)


def validate_ratios(
    ratios: list[int],
) -> None:
    """
    Valida os pesos utilizados na alocação.
    """

    if not ratios:
        raise EmptyAllocationError(
            "Nenhuma razão de alocação foi informada."
        )

    if any(ratio <= 0 for ratio in ratios):
        raise InvalidAllocationRatioError(
            "Todas as razões devem ser maiores que zero."
        )


def total_ratio(
    ratios: list[int],
) -> int:
    """
    Retorna a soma total dos pesos.
    """

    validate_ratios(ratios)

    return sum(ratios)
