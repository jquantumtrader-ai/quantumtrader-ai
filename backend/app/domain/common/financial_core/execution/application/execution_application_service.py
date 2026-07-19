from __future__ import annotations

from decimal import Decimal
from uuid import UUID, uuid4

from ..enums import ExecutionStatus
from ..events import ExecutionEvent
from ..publishers import ExecutionEventPublisher
from ..unit_of_work import ExecutionUnitOfWork


class ExecutionApplicationService:
    """
    Serviço de aplicação responsável pelos
    casos de uso de execução.
    """


    def __init__(
        self,
        unit_of_work: ExecutionUnitOfWork,
        event_publisher: ExecutionEventPublisher,
    ) -> None:

        self._unit_of_work = unit_of_work

        self._event_publisher = event_publisher



    def _publish_events(
        self,
        execution,
    ) -> None:
        """
        Publica eventos pendentes do aggregate.
        """

        events = execution.pull_events()


        self._event_publisher.publish(
            events,
        )



    def create_execution(
        self,
        quantity: Decimal,
    ) -> UUID:

        self._unit_of_work.begin()

        try:

            execution_id = uuid4()


            execution = self._unit_of_work.repository.create(
                execution_id,
                quantity,
            )


            self._unit_of_work.repository.save(
                execution,
            )


            self._publish_events(
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


            self._publish_events(
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


            self._publish_events(
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

        execution = (
            self._unit_of_work.repository.get(
                execution_id,
            )
        )


        return execution.pull_events()
