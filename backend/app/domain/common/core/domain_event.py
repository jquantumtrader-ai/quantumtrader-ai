from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Mapping
from uuid import UUID


@dataclass(frozen=True, slots=True)
class DomainEvent:
    """
    Evento base do domínio.

    Todos os eventos do sistema devem
    herdar desta classe.
    """

    aggregate_id: UUID

    event_type: str

    occurred_at: datetime = field(
        default_factory=datetime.utcnow,
    )

    payload: Mapping[str, object] = field(
        default_factory=dict,
    )
