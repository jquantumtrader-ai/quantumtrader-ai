from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.enums import ExecutionStatus
from app.domain.common.financial_core.execution.events import (
    ExecutionCancelledEvent,
    ExecutionCreatedEvent,
    ExecutionFilledEvent,
)
from app.domain.common.financial_core.execution.replay import (
    ExecutionEventReplayService,
)


def test_replay_created_event():

    execution_id = uuid4()

    replay = ExecutionEventReplayService()

    aggregate = replay.replay(
        [
            ExecutionCreatedEvent(
                execution_id=execution_id,
                quantity=Decimal("100"),
            ),
        ],
    )

    assert aggregate.execution_id == execution_id
    assert aggregate.quantity == Decimal("100")
    assert aggregate.filled_quantity == Decimal("0")
    assert aggregate.status == ExecutionStatus.CREATED


def test_replay_partial_fill():

    execution_id = uuid4()

    replay = ExecutionEventReplayService()

    aggregate = replay.replay(
        [
            ExecutionCreatedEvent(
                execution_id=execution_id,
                quantity=Decimal("100"),
            ),
            ExecutionFilledEvent(
                execution_id=execution_id,
                quantity=Decimal("40"),
            ),
        ],
    )

    assert aggregate.filled_quantity == Decimal("40")
    assert aggregate.status == ExecutionStatus.PARTIAL


def test_replay_complete_fill():

    execution_id = uuid4()

    replay = ExecutionEventReplayService()

    aggregate = replay.replay(
        [
            ExecutionCreatedEvent(
                execution_id=execution_id,
                quantity=Decimal("100"),
            ),
            ExecutionFilledEvent(
                execution_id=execution_id,
                quantity=Decimal("100"),
            ),
        ],
    )

    assert aggregate.status == ExecutionStatus.FILLED


def test_replay_cancelled():

    execution_id = uuid4()

    replay = ExecutionEventReplayService()

    aggregate = replay.replay(
        [
            ExecutionCreatedEvent(
                execution_id=execution_id,
                quantity=Decimal("100"),
            ),
            ExecutionCancelledEvent(
                execution_id=execution_id,
                reason="Broker cancelled",
            ),
        ],
    )

    assert aggregate.status == ExecutionStatus.CANCELLED


def test_replay_without_created_event():

    replay = ExecutionEventReplayService()

    with pytest.raises(
        ValueError,
    ):

        replay.replay(
            [],
        )
