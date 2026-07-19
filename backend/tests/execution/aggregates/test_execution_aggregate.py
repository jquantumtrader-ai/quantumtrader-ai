from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.aggregates import (
    ExecutionAggregate,
)

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)


def test_create_execution_aggregate():

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    assert aggregate.status == (
        ExecutionStatus.CREATED
    )

    assert len(
        aggregate.pull_events(),
    ) == 1



def test_partial_fill():

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    aggregate.pull_events()

    aggregate.add_fill(
        Decimal("40"),
    )

    assert aggregate.filled_quantity == Decimal(
        "40",
    )

    assert aggregate.status == (
        ExecutionStatus.PARTIAL
    )



def test_complete_fill():

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    aggregate.pull_events()

    aggregate.add_fill(
        Decimal("100"),
    )

    assert aggregate.status == (
        ExecutionStatus.FILLED
    )

    assert len(
        aggregate.pull_events(),
    ) == 1



def test_cancel_execution():

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    aggregate.pull_events()

    aggregate.cancel(
        "Broker rejected",
    )

    assert aggregate.status == (
        ExecutionStatus.CANCELLED
    )


def test_fill_overflow():

    aggregate = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )

    with pytest.raises(
        ValueError,
    ):

        aggregate.add_fill(
            Decimal("200"),
        )
