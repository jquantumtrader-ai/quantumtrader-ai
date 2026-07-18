from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ..entities.order import Order
from ..enums.order_status import OrderStatus



@dataclass(
    frozen=True
)
class OrderDomainService:
    """
    Serviço de domínio responsável
    por regras que envolvem ordens.
    """



    def can_execute(
        self,
        order: Order,
    ) -> bool:
        """
        Verifica se uma ordem pode
        entrar em execução.
        """

        return (
            order.status
            in (
                OrderStatus.CREATED,
                OrderStatus.PARTIALLY_FILLED,
            )
        )



    def can_cancel(
        self,
        order: Order,
    ) -> bool:
        """
        Verifica se uma ordem
        pode ser cancelada.
        """

        return (
            order.status
            not in (
                OrderStatus.FILLED,
                OrderStatus.CANCELLED,
                OrderStatus.REJECTED,
            )
        )



    def remaining_quantity(
        self,
        order: Order,
    ) -> Decimal:
        """
        Calcula quantidade restante.
        """

        filled = sum(
            fill.quantity
            for fill in order.fills
        )


        remaining = (
            order.quantity
            -
            filled
        )


        if remaining < Decimal("0"):
            return Decimal("0")


        return remaining



    def is_completed(
        self,
        order: Order,
    ) -> bool:
        """
        Verifica se a ordem
        foi totalmente concluída.
        """

        if (
            order.status
            ==
            OrderStatus.FILLED
        ):
            return True


        return (
            self.remaining_quantity(
                order
            )
            ==
            Decimal("0")
        )
