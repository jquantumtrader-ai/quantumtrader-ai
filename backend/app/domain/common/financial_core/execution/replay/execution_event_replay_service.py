from __future__ import annotations

from decimal import Decimal
from typing import Iterable, cast

from ..aggregates import ExecutionAggregate
from ..events import (
    ExecutionCancelledEvent,
    ExecutionCreatedEvent,
    ExecutionFilledEvent,
)


class ExecutionEventReplayService:
    """
    Reconstrói um ExecutionAggregate
    a partir do histórico de eventos.

    Base para Event Sourcing.
    """

    def replay(
        self,
        events: Iterable[object],
    ) -> ExecutionAggregate:
        """
        Reconstrói um Aggregate
        utilizando uma sequência
        de eventos.
        """

        aggregate: ExecutionAggregate | None = None

        for event in events:

            if isinstance(
                event,
                ExecutionCreatedEvent,
            ):

                quantity = cast(
                    Decimal,
                    event.payload["quantity"],
                )

                aggregate = ExecutionAggregate(
                    execution_id=event.execution_id,
                    quantity=quantity,
                )

                # Remove o evento criado
                # automaticamente pelo Aggregate.
                aggregate.pull_events()

                continue

            if aggregate is None:

                raise ValueError(
                    "ExecutionCreatedEvent must be the first event."
                )

            if isinstance(
                event,
                ExecutionFilledEvent,
            ):

                aggregate.add_fill(
                    cast(
                        Decimal,
                        event.payload["quantity"],
                    )
                )

                aggregate.pull_events()

                continue

            if isinstance(
                event,
                ExecutionCancelledEvent,
            ):

                aggregate.cancel(
                    cast(
                        str,
                        event.payload["reason"],
                    )
                )

                aggregate.pull_events()

                continue

        if aggregate is None:

            raise ValueError(
                "No ExecutionCreatedEvent found."
            )

        return aggregate
