from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID

from ..enums import ExecutionStatus
from ..events import (
    ExecutionEvent,
    ExecutionCreatedEvent,
    ExecutionFilledEvent,
    ExecutionCancelledEvent,
)
from ..state import ExecutionStateTransition


@dataclass
class ExecutionAggregate:
    """
    Aggregate Root da execução.
    """

    execution_id: UUID

    quantity: Decimal

    status: ExecutionStatus = ExecutionStatus.CREATED

    filled_quantity: Decimal = Decimal("0")

    version: int = 0

    _events: list[ExecutionEvent] = field(
        default_factory=list,
        init=False,
    )

    def __post_init__(self) -> None:

        self._events.append(
            ExecutionCreatedEvent(
                execution_id=self.execution_id,
                quantity=self.quantity,
            )
        )

        self.version = 1

    def change_status(
        self,
        new_status: ExecutionStatus,
    ) -> None:

        ExecutionStateTransition.validate(
            self.status,
            new_status,
        )

        self.status = new_status

    def activate(self) -> None:

        if self.status == ExecutionStatus.CREATED:

            self.change_status(
                ExecutionStatus.PENDING,
            )

    def add_fill(
        self,
        quantity: Decimal,
    ) -> None:

        if self.status == ExecutionStatus.CREATED:
            self.activate()

        new_quantity = (
            self.filled_quantity
            + quantity
        )

        if new_quantity > self.quantity:

            raise ValueError(
                "Fill exceeds execution quantity"
            )

        self.filled_quantity = new_quantity

        if self.filled_quantity == self.quantity:

            self.change_status(
                ExecutionStatus.FILLED,
            )

            self._events.append(
                ExecutionFilledEvent(
                    execution_id=self.execution_id,
                    quantity=self.quantity,
                )
            )

        else:

            self.change_status(
                ExecutionStatus.PARTIAL,
            )

        self.version += 1

    def cancel(
        self,
        reason: str,
    ) -> None:

        if self.status == ExecutionStatus.CREATED:
            self.activate()

        self.change_status(
            ExecutionStatus.CANCELLED,
        )

        self._events.append(
            ExecutionCancelledEvent(
                execution_id=self.execution_id,
                reason=reason,
            )
        )

        self.version += 1

    def pull_events(
        self,
    ) -> list[ExecutionEvent]:

        events = list(
            self._events,
        )

        self._events.clear()

        return events
