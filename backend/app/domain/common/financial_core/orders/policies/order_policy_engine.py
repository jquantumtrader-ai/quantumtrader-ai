from __future__ import annotations

from dataclasses import dataclass

from ..entities.order import Order

from ..specifications import (
    OrderCanExecuteSpecification,
    OrderCanCancelSpecification,
    OrderCompletedSpecification,
)



@dataclass(
    frozen=True
)
class OrderPolicyEngine:
    """
    Motor de políticas de ordem.

    Centraliza decisões baseadas
    nas regras de domínio.
    """



    can_execute_policy: OrderCanExecuteSpecification = (
        OrderCanExecuteSpecification()
    )


    can_cancel_policy: OrderCanCancelSpecification = (
        OrderCanCancelSpecification()
    )


    completed_policy: OrderCompletedSpecification = (
        OrderCompletedSpecification()
    )



    def can_execute(
        self,
        order: Order,
    ) -> bool:
        """
        Verifica se pode executar.
        """

        return (
            self.can_execute_policy
            .is_satisfied_by(
                order
            )
        )



    def can_cancel(
        self,
        order: Order,
    ) -> bool:
        """
        Verifica se pode cancelar.
        """

        return (
            self.can_cancel_policy
            .is_satisfied_by(
                order
            )
        )



    def is_completed(
        self,
        order: Order,
    ) -> bool:
        """
        Verifica conclusão.
        """

        return (
            self.completed_policy
            .is_satisfied_by(
                order
            )
        )
