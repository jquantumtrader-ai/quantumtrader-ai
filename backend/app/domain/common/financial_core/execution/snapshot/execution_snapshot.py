from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from ..enums import ExecutionStatus


@dataclass(frozen=True, slots=True)
class ExecutionSnapshot:
    """
    Snapshot imutável do estado da execução.
    """

    execution_id: UUID

    quantity: Decimal

    filled_quantity: Decimal

    status: ExecutionStatus

    created_at: datetime
