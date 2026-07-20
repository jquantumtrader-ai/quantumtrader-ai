from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ExecutionSnapshot:
    """
    Snapshot imutável do estado de uma Execution.

    Permite reconstruir rapidamente um Aggregate sem
    reproduzir todo o histórico de eventos.
    """

    execution_id: UUID
    quantity: Decimal
    filled_quantity: Decimal
    cancelled: bool
    created_at: datetime
