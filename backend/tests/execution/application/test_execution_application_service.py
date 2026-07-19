from decimal import Decimal

import pytest

from app.domain.common.financial_core.execution.adapters import (
    InMemoryExecutionRepository,
)

from app.domain.common.financial_core.execution.application import (
    ExecutionApplicationService,
)

from app.domain.common.financial_core.execution.enums import (
    ExecutionStatus,
)

from app.domain.common.financial_core.execution.event_store import (
    InMemoryEventStore,
)

from app.domain.common.financial_core.execution.publishers import (
    ExecutionEventPublisher,
)

from app.domain.common.financial_core.execution.unit_of_work import (
    ExecutionUnitOfWork,
)



def create_service() -> ExecutionApplicationService:
    """
    Cria Application Service completo.

    Stack:

    ApplicationService
            |
            ▼
    UnitOfWork
            |
            ▼
    Repository

    +

    EventPublisher
            |
            ▼
    EventStore
    """

    repository = InMemoryExecutionRepository()


    unit_of_work = ExecutionUnitOfWork(
        repository,
    )


    event_store = InMemoryEventStore()


    publisher = ExecutionEventPublisher(
        event_store,
    )


    return ExecutionApplicationService(
        unit_of_work,
        publisher,
    )



def test_create_execution():

    service = create_service()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    status = service.get_status(
        execution_id,
    )


    assert status == ExecutionStatus.CREATED



def test_add_fill():

    service = create_service()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    service.add_fill(
        execution_id,
        Decimal("100"),
    )


    status = service.get_status(
        execution_id,
    )


    assert status == ExecutionStatus.FILLED



def test_partial_fill():

    service = create_service()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    service.add_fill(
        execution_id,
        Decimal("40"),
    )


    status = service.get_status(
        execution_id,
    )


    assert status == ExecutionStatus.PARTIAL



def test_cancel_execution():

    service = create_service()


    execution_id = service.create_execution(
        Decimal("100"),
    )


    service.cancel_execution(
        execution_id,
        "Broker rejected",
    )


    status = service.get_status(
        execution_id,
    )


    assert status == ExecutionStatus.CANCELLED



def test_invalid_execution():

    service = create_service()


    with pytest.raises(
        Exception,
    ):

        service.get_status(
            "invalid",
        )
