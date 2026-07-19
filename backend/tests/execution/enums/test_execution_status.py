from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)


def test_execution_status_values():

    assert ExecutionStatus.CREATED.value == "CREATED"

    assert ExecutionStatus.PENDING.value == "PENDING"

    assert ExecutionStatus.PARTIAL.value == "PARTIAL"

    assert ExecutionStatus.FILLED.value == "FILLED"

    assert ExecutionStatus.REJECTED.value == "REJECTED"

    assert ExecutionStatus.CANCELLED.value == "CANCELLED"


def test_execution_status_enum():

    assert (
        ExecutionStatus.FILLED
        ==
        ExecutionStatus.FILLED
    )

    assert (
        ExecutionStatus.CREATED
        !=
        ExecutionStatus.FILLED
    )
