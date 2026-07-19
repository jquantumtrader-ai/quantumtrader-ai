from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.adapters import (
    InMemoryExecutionRepository,
)

from app.domain.common.financial_core.execution.aggregates import (
    ExecutionAggregate,
)



def test_save_and_get_execution():

    repository = (
        InMemoryExecutionRepository()
    )


    execution = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )


    repository.save(
        execution,
    )


    loaded = repository.get(
        execution.execution_id,
    )


    assert loaded == execution



def test_exists_execution():

    repository = (
        InMemoryExecutionRepository()
    )


    execution = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("50"),
    )


    assert not repository.exists(
        execution.execution_id,
    )


    repository.save(
        execution,
    )


    assert repository.exists(
        execution.execution_id,
    )



def test_remove_execution():

    repository = (
        InMemoryExecutionRepository()
    )


    execution = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("20"),
    )


    repository.save(
        execution,
    )


    repository.remove(
        execution.execution_id,
    )


    assert not repository.exists(
        execution.execution_id,
    )



def test_get_missing_execution():

    repository = (
        InMemoryExecutionRepository()
    )


    with pytest.raises(
        ValueError,
    ):

        repository.get(
            uuid4(),
        )



def test_clear_repository():

    repository = (
        InMemoryExecutionRepository()
    )


    execution = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("10"),
    )


    repository.save(
        execution,
    )


    repository.clear()


    assert not repository.exists(
        execution.execution_id,
    )
