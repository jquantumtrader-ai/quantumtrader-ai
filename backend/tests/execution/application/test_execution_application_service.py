from decimal import Decimal

import pytest

from app.domain.common.financial_core.execution.application import (
    ExecutionApplicationService,
)

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)



def test_create_execution():

    service = ExecutionApplicationService()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    assert (
        service.get_status(execution_id)
        ==
        ExecutionStatus.CREATED
    )


    events = service.collect_events(
        execution_id,
    )


    assert len(events) == 1



def test_add_fill():

    service = ExecutionApplicationService()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    service.collect_events(
        execution_id,
    )


    service.add_fill(
        execution_id,
        Decimal("100"),
    )


    assert (
        service.get_status(execution_id)
        ==
        ExecutionStatus.FILLED
    )



def test_cancel_execution():

    service = ExecutionApplicationService()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    service.cancel_execution(
        execution_id,
        "Broker rejected",
    )


    assert (
        service.get_status(execution_id)
        ==
        ExecutionStatus.CANCELLED
    )



def test_invalid_execution():

    service = ExecutionApplicationService()


    with pytest.raises(
        ValueError,
    ):

        service.get_status(
            "invalid",
        )
