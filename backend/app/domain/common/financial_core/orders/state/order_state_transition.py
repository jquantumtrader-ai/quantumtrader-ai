from __future__ import annotations

from ..enums import OrderStatus


class InvalidOrderTransition(
    ValueError,
):
    """
    Exceção lançada quando uma transição
    de estado de ordem não é permitida.
    """



class OrderStateTransition:
    """
    Responsável pelas regras de transição
    do ciclo de vida de uma ordem.
    """


    _allowed_transitions: dict[
        OrderStatus,
        set[OrderStatus],
    ] = {

        OrderStatus.CREATED: {
            OrderStatus.SUBMITTED,
            OrderStatus.CANCELLED,
            OrderStatus.REJECTED,
        },

        OrderStatus.SUBMITTED: {
            OrderStatus.PARTIALLY_FILLED,
            OrderStatus.FILLED,
            OrderStatus.CANCELLED,
            OrderStatus.REJECTED,
        },

        OrderStatus.PARTIALLY_FILLED: {
            OrderStatus.FILLED,
            OrderStatus.CANCELLED,
        },

        OrderStatus.FILLED: set(),

        OrderStatus.CANCELLED: set(),

        OrderStatus.REJECTED: set(),
    }


    @classmethod
    def can_transition(
        cls,
        current: OrderStatus,
        target: OrderStatus,
    ) -> bool:
        """
        Verifica se uma mudança de estado
        é permitida.
        """

        return (
            target
            in cls._allowed_transitions.get(
                current,
                set(),
            )
        )


    @classmethod
    def validate(
        cls,
        current: OrderStatus,
        target: OrderStatus,
    ) -> None:
        """
        Valida uma transição de estado.

        Levanta exceção quando inválida.
        """

        if not cls.can_transition(
            current,
            target,
        ):

            raise InvalidOrderTransition(
                f"Transição inválida: "
                f"{current.value} -> {target.value}"
            )
