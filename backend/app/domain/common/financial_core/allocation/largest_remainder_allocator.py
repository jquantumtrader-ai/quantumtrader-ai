from __future__ import annotations

from decimal import Decimal
from decimal import ROUND_DOWN

from ..value_objects.money import Money
from .allocator import MoneyAllocator
from .utils import total_ratio


class LargestRemainderAllocator(MoneyAllocator):
    """
    Implementa o algoritmo Largest Remainder Method.

    Características:

    - Usa Decimal
    - Mantém precisão financeira
    - Distribuição determinística
    - Conserva o valor total
    """

    def allocate(
        self,
        money: Money,
        ratios: list[int],
    ) -> list[Money]:

        ratio_sum = total_ratio(ratios)

        proportional = (
            self._calculate_proportional_values(
                money,
                ratios,
                ratio_sum,
            )
        )

        base_values = (
            self._calculate_base_values(
                proportional,
            )
        )

        remainders = (
            self._calculate_remainders(
                proportional,
                base_values,
            )
        )

        return self._distribute_remainder(
            money,
            base_values,
            remainders,
        )

    def _calculate_proportional_values(
        self,
        money: Money,
        ratios: list[int],
        ratio_sum: int,
    ) -> list[Decimal]:

        return [
            (
                money.value
                * Decimal(ratio)
                / Decimal(ratio_sum)
            )
            for ratio in ratios
        ]

    def _calculate_base_values(
        self,
        values: list[Decimal],
    ) -> list[Decimal]:

        return [
            value.quantize(
                Money.SCALE,
                rounding=ROUND_DOWN,
            )
            for value in values
        ]

    def _calculate_remainders(
        self,
        proportional: list[Decimal],
        base_values: list[Decimal],
    ) -> list[tuple[int, Decimal]]:

        return [
            (
                index,
                proportional[index]
                - base_values[index],
            )
            for index in range(
                len(proportional)
            )
        ]

    def _distribute_remainder(
        self,
        original: Money,
        base_values: list[Decimal],
        remainders: list[tuple[int, Decimal]],
    ) -> list[Money]:

        allocated = sum(base_values)

        remaining = (
            original.value
            - allocated
        )

        increment = Money.SCALE

        ordered = sorted(
            remainders,
            key=lambda item: (
                -item[1],
                item[0],
            ),
        )

        values = list(base_values)

        index = 0

        while remaining > Decimal("0"):

            target = ordered[index][0]

            values[target] += increment

            remaining -= increment

            index += 1

            if index >= len(ordered):
                index = 0

        return [
            Money(
                value,
                original.currency,
            )
            for value in values
        ]
