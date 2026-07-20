from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.aggregates import (
    ExecutionAggregate,
)


def test_version_increments() -> None:

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    assert int(aggregate.version) == 1

    aggregate.pull_events()

    aggregate.add_fill(
        Decimal("20"),
    )

    assert int(aggregate.version) == 2

    aggregate.cancel(
        "user",
    )

    assert int(aggregate.version) == 3
