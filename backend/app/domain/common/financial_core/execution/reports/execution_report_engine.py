from __future__ import annotations

from decimal import Decimal

from .execution_report import ExecutionReport
from ..enums import ExecutionStatus


class ExecutionReportEngine:
    """
    Motor responsável por gerar
    relatórios consolidados de execução.
    """

    def generate(
        self,
        fills: list[tuple[Decimal, Decimal]],
        requested_quantity: Decimal,
    ) -> ExecutionReport:
        """
        Gera relatório a partir dos fills.

        Cada fill:
        (quantidade, preço)
        """

        if not fills:
            raise ValueError(
                "Execution requires fills"
            )

        total_quantity = Decimal("0")

        total_value = Decimal("0")

        for quantity, price in fills:
            total_quantity += quantity
            total_value += (
                quantity * price
            )

        average_price = (
            total_value / total_quantity
        )

        completed = (
            total_quantity
            ==
            requested_quantity
        )

        status = (
            ExecutionStatus.FILLED
            if completed
            else ExecutionStatus.PARTIAL
        )

        return ExecutionReport(
            total_quantity=total_quantity,
            average_price=average_price,
            status=status,
            completed=completed,
        )
