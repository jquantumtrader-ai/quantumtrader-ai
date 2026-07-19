from __future__ import annotations

from decimal import Decimal
from uuid import UUID, uuid4

from ..aggregates import ExecutionAggregate
from ..enums import ExecutionStatus
from ..events import ExecutionEvent
from ..ports import ExecutionRepository


class ExecutionApplicationService:
    """
    Serviço de aplicação responsável por
    coordenar casos de uso de execução.
    """

    def __init__(
        self,
        repository: ExecutionRepository,
    ) -> None:

        self._repository = repository


    def create_execution(
        self,
        quantity: Decimal,
    ) -> UUID:
        """
        Cria uma execução.
        """

        execution_id = uuid4()

        execution = ExecutionAggregate(
            execution_id=execution_id,
            quantity=quantity,
        )

        self._repository.save(
            execution,
        )

        return execution_id



    def add_fill(
        self,
        execution_id: UUID,
        quantity: Decimal,
    ) -> None:
        """
        Adiciona preenchimento.
        """

        execution = self._repository.get(
            execution_id,
        )


        execution.add_fill(
            quantity,
        )


        self._repository.save(
            execution,
        )



    def cancel_execution(
        self,
        execution_id: UUID,
        reason: str,
    ) -> None:
        """
        Cancela execução.
        """

        execution = self._repository.get(
            execution_id,
        )


        execution.cancel(
            reason,
        )


        self._repository.save(
            execution,
        )



    def get_status(
        self,
        execution_id: UUID,
    ) -> ExecutionStatus:
        """
        Retorna status.
        """

        execution = self._repository.get(
            execution_id,
        )

        return execution.status



    def collect_events(
        self,
        execution_id: UUID,
    ) -> list[ExecutionEvent]:
        """
        Coleta eventos.
        """

        execution = self._repository.get(
            execution_id,
        )

        return execution.pull_events()
