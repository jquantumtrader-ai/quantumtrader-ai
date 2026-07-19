from uuid import UUID

from .execution_event import ExecutionEvent


class ExecutionCancelledEvent(ExecutionEvent):
    """
    Evento disparado quando uma execução
    é cancelada.
    """

    def __init__(
        self,
        execution_id: UUID,
        reason: str,
    ) -> None:

        super().__init__(
            execution_id=execution_id,
            event_type="EXECUTION_CANCELLED",
            payload={
                "reason": reason,
            },
        )
