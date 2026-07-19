from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..enums import ExecutionStatus


@dataclass(frozen=True, slots=True)
class ExecutionReport:
    """
    Representa o resumo consolidado
    de uma execução.
    """

    total_quantity: Decimal

    average_price: Decimal

    status: ExecutionStatus

    completed: bool
