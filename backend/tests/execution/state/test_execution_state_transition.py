import pytest

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)

from app.domain.common.financial_core.execution.state import (
    ExecutionStateTransition,
    InvalidExecutionTransition,
)



def test_valid_transition():

    assert (
        ExecutionStateTransition.can_transition(
            ExecutionStatus.CREATED,
            ExecutionStatus.PENDING,
        )
        is True
    )



def test_partial_to_filled():

    ExecutionStateTransition.validate(
        ExecutionStatus.PARTIAL,
        ExecutionStatus.FILLED,
    )



def test_invalid_transition():

    with pytest.raises(
        InvalidExecutionTransition,
    ):

        ExecutionStateTransition.validate(
            ExecutionStatus.CREATED,
            ExecutionStatus.FILLED,
        )



def test_filled_cannot_change():

    assert (
        ExecutionStateTransition.can_transition(
            ExecutionStatus.FILLED,
            ExecutionStatus.CANCELLED,
        )
        is False
    )
