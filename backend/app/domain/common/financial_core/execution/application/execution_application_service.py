from __future__ import annotations

from decimal import Decimal
from uuid import UUID, uuid4

from ..enums import ExecutionStatus
from ..events import ExecutionEvent
from ..unit_of_work import ExecutionUnitOfWork
from ..aggregates import ExecutionAggregate


class ExecutionApplicationService:
    """
    Serviço de aplicação responsável pelos
    casos de uso de execução.
    """

    def __init__(
        self,
        unit_of_work: ExecutionUnitOfWork,
    ) -> None:

        self._unit_of_work = unit_of_work



    def create_execution(
        self,
        quantity: Decimal,
    ) -> UUID:
        """
        Cria uma execução.
        """

        self._unit_of_work.begin()

        try:

            execution_id = uuid4()

            execution = ExecutionAggregate(
                execution_id=execution_id,
                quantity=quantity,
            )


            self._unit_of_work.repository.save(
                execution,
            )


            self._unit_of_work.commit()


            return execution_id


        except Exception:

            self._unit_of_work.rollback()

            raise



    def add_fill(
        self,
        execution_id: UUID,
        quantity: Decimal,
    ) -> None:
        """
        Adiciona preenchimento.
        """

        self._unit_of_work.begin()

        try:

            execution = (
                self._unit_of_work.repository.get(
                    execution_id,
                )
            )


            execution.add_fill(
                quantity,
            )


            self._unit_of_work.repository.save(
                execution,
            )


            self._unit_of_work.commit()


        except Exception:

            self._unit_of_work.rollback()

            raise



    def cancel_execution(
        self,
        execution_id: UUID,
        reason: str,
    ) -> None:
        """
        Cancela execução.
        """

        self._unit_of_work.begin()

        try:

            execution = (
                self._unit_of_work.repository.get(
                    execution_id,
                )
            )


            execution.cancel(
                reason,
            )


            self._unit_of_work.repository.save(
                execution,
            )


            self._unit_of_work.commit()


        except Exception:

            self._unit_of_work.rollback()

            raise



    def get_status(
        self,
        execution_id: UUID,
    ) -> ExecutionStatus:
        """
        Retorna status.
        """

        execution = (
            self._unit_of_work.repository.get(
                execution_id,
            )
        )


        return execution.status



    def collect_events(
        self,
        execution_id: UUID,
    ) -> list[ExecutionEvent]:
        """
        Coleta eventos.
        """

        execution = (
            self._unit_of_work.repository.get(
                execution_id,
            )
        )


        return execution.pull_events()
