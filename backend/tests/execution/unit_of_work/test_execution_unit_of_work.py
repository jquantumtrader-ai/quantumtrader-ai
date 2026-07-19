from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.adapters import (
    InMemoryExecutionRepository,
)

from app.domain.common.financial_core.execution.aggregates import (
    ExecutionAggregate,
)

from app.domain.common.financial_core.execution.unit_of_work import (
    ExecutionUnitOfWork,
)



def create_uow():

    repository = (
        InMemoryExecutionRepository()
    )


    return ExecutionUnitOfWork(
        repository,
    )



def test_begin_transaction():

    uow = create_uow()


    uow.begin()


    assert uow.is_active



def test_commit_transaction():

    uow = create_uow()


    uow.begin()

    uow.commit()


    assert uow.is_committed

    assert not uow.is_active



def test_rollback_transaction():

    uow = create_uow()


    uow.begin()

    uow.rollback()


    assert uow.is_rolled_back

    assert not uow.is_active



def test_repository_access():

    uow = create_uow()


    execution = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )


    uow.begin()


    uow.repository.save(
        execution,
    )


    loaded = uow.repository.get(
        execution.execution_id,
    )


    assert loaded == execution



def test_commit_without_begin():

    uow = create_uow()


    with pytest.raises(
        RuntimeError,
    ):

        uow.commit()
