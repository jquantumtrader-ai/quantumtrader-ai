from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, order=True)
class AggregateVersion:
    """
    Value Object que representa
    a versão de um Aggregate.
    """

    value: int = 0

    def __post_init__(
        self,
    ) -> None:

        if self.value < 0:

            raise ValueError(
                "Aggregate version cannot be negative."
            )

    def next(
        self,
    ) -> "AggregateVersion":

        return AggregateVersion(
            self.value + 1,
        )

    def __int__(
        self,
    ) -> int:

        return self.value

    def __str__(
        self,
    ) -> str:

        return str(
            self.value,
        )
