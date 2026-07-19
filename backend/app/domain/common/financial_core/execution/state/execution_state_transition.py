from __future__ import annotations

from ..enums import ExecutionStatus


class InvalidExecutionTransition(Exception):
    """
    Exceção lançada quando uma execução
    tenta realizar uma transição inválida.
    """



class ExecutionStateTransition:
    """
    Responsável pelas regras de transição
    do ciclo de vida de uma execução.
    """

    _transitions: dict[
        ExecutionStatus,
        set[ExecutionStatus],
    ] = {
        ExecutionStatus.CREATED: {
            ExecutionStatus.PENDING,
        },

        ExecutionStatus.PENDING: {
            ExecutionStatus.PARTIAL,
            ExecutionStatus.FILLED,
            ExecutionStatus.REJECTED,
            ExecutionStatus.CANCELLED,
        },

        ExecutionStatus.PARTIAL: {
            ExecutionStatus.FILLED,
            ExecutionStatus.CANCELLED,
        },

        ExecutionStatus.FILLED: set(),

        ExecutionStatus.REJECTED: set(),

        ExecutionStatus.CANCELLED: set(),
    }


    @classmethod
    def can_transition(
        cls,
        current: ExecutionStatus,
        target: ExecutionStatus,
    ) -> bool:
        """
        Verifica se uma transição é permitida.
        """

        return (
            target
            in cls._transitions.get(
                current,
                set(),
            )
        )


    @classmethod
    def validate(
        cls,
        current: ExecutionStatus,
        target: ExecutionStatus,
    ) -> None:
        """
        Valida uma transição.

        Levanta exceção caso seja inválida.
        """

        if not cls.can_transition(
            current,
            target,
        ):
            raise InvalidExecutionTransition(
                f"Invalid execution transition: "
                f"{current.value} -> {target.value}"
            )
