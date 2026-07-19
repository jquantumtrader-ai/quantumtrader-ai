from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution.aggregates import (
    ExecutionAggregate,
)

from app.domain.common.financial_core.execution.ports import (
    ExecutionRepository,
)


class InMemoryExecutionRepository:
    """
    Implementação fake apenas para validar
    o contrato do port.
    """

    def __init__(self) -> None:

        self.storage = {}


    def save(
        self,
        execution,
    ) -> None:

        self.storage[
            execution.execution_id
        ] = execution


    def get(
        self,
        execution_id,
    ):

        return self.storage[
            execution_id
        ]


    def exists(
        self,
        execution_id,
    ):

        return execution_id in self.storage


    def remove(
        self,
        execution_id,
    ) -> None:

        del self.storage[
            execution_id
        ]



def test_repository_contract():

    repository: ExecutionRepository = (
        InMemoryExecutionRepository()
    )


    execution = ExecutionAggregate(
        execution_id=uuid4(),
        quantity=Decimal("100"),
    )


    repository.save(
        execution,
    )


    assert repository.exists(
        execution.execution_id,
    )


    loaded = repository.get(
        execution.execution_id,
    )


    assert loaded == execution


    repository.remove(
        execution.execution_id,
    )


    assert not repository.exists(
        execution.execution_id,
    )
