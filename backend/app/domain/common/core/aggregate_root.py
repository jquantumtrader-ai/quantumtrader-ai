from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from app.domain.common.financial_core.execution.value_objects import (
    AggregateVersion,
)

from .domain_event import DomainEvent

TId = TypeVar("TId")


class AggregateRoot(ABC, Generic[TId]):
    """
    Classe base para todos os Aggregate Roots.

    Responsabilidades
    -----------------
    • Controlar a versão do Aggregate.
    • Registrar Domain Events.
    • Expor eventos pendentes.
    """

    def __init__(self) -> None:
        self._version = AggregateVersion.initial()
        self._events: list[DomainEvent] = []

    @property
    def version(self) -> AggregateVersion:
        return self._version

    @version.setter
    def version(self, value: AggregateVersion) -> None:
        self._version = value

    @property
    def events(self) -> tuple[DomainEvent, ...]:
        return tuple(self._events)

    def record_event(self, event: DomainEvent) -> None:
        self._events.append(event)
        self._version = self._version.next()

    def pull_events(self) -> list[DomainEvent]:
        events = self._events.copy()
        self._events.clear()
        return events

    def clear_events(self) -> None:
        self._events.clear()
