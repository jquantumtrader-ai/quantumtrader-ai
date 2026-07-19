from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ExecutionEvent:
    """
    Evento base do domínio de execução.
    """

    execution_id: UUID

    event_type: str

    occurred_at: datetime = field(
        default_factory=datetime.utcnow,
    )

    payload: dict[str, object] = field(
        default_factory=dict,
    )
