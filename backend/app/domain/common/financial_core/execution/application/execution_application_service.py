from __future__ import annotations

from decimal import Decimal
from uuid import UUID, uuid4

from ..aggregates import ExecutionAggregate
from ..enums import ExecutionStatus
from ..events import ExecutionEvent


class ExecutionApplicationService:
    """
    Serviço de aplicação responsável por
    orquestrar operações de execução.
    """

    def __init__(self) -> None:

        self._executions: dict[
            UUID,
            ExecutionAggregate,
        ] = {}


    def create_execution(
        self,
        quantity: Decimal,
    ) -> UUID:
        """
        Cria uma nova execução.
        """

        execution_id = uuid4()

        aggregate = ExecutionAggregate(
            execution_id=execution_id,
            quantity=quantity,
        )

        self._executions[
            execution_id
        ] = aggregate


        return execution_id



    def add_fill(
        self,
        execution_id: UUID,
        quantity: Decimal,
    ) -> None:
        """
        Adiciona preenchimento
        à execução.
        """

        execution = self._get_execution(
            execution_id,
        )

        execution.add_fill(
            quantity,
        )



    def cancel_execution(
        self,
        execution_id: UUID,
        reason: str,
    ) -> None:
        """
        Cancela uma execução.
        """

        execution = self._get_execution(
            execution_id,
        )

        execution.cancel(
            reason,
        )



    def get_status(
        self,
        execution_id: UUID,
    ) -> ExecutionStatus:
        """
        Retorna status atual.
        """

        execution = self._get_execution(
            execution_id,
        )

        return execution.status



    def collect_events(
        self,
        execution_id: UUID,
    ) -> list[ExecutionEvent]:
        """
        Retorna eventos gerados.
        """

        execution = self._get_execution(
            execution_id,
        )

        return execution.pull_events()



    def _get_execution(
        self,
        execution_id: UUID,
    ) -> ExecutionAggregate:

        try:

            return self._executions[
                execution_id
            ]

        except KeyError as exc:

            raise ValueError(
                "Execution not found"
            ) from exc
