from uuid import UUID

from .execution_event import ExecutionEvent


class ExecutionCreatedEvent(ExecutionEvent):
    """
    Evento disparado quando uma execução
    é criada.
    """

    def __init__(
        self,
        execution_id: UUID,
    ) -> None:

        super().__init__(
            execution_id=execution_id,
            event_type="EXECUTION_CREATED",
        )
