from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ...portfolio.assets.asset import Asset
from ...value_objects.money import Money
from ..enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from ..order_id import OrderId
from ..state import OrderStateTransition



@dataclass(frozen=True)
class Order:
    """
    Representa uma ordem financeira
    dentro do domínio.
    """


    order_id: OrderId

    asset: Asset

    side: OrderSide

    order_type: OrderType

    status: OrderStatus

    quantity: Decimal

    price: Money



    def __post_init__(
        self,
    ) -> None:

        if self.quantity <= Decimal("0"):

            raise ValueError(
                "Quantidade deve ser maior que zero."
            )



    @property
    def notional(
        self,
    ) -> Money:

        return Money(
            self.quantity
            *
            self.price.value,
            self.price.currency,
        )



    @property
    def is_buy(
        self,
    ) -> bool:

        return (
            self.side
            ==
            OrderSide.BUY
        )



    @property
    def is_sell(
        self,
    ) -> bool:

        return (
            self.side
            ==
            OrderSide.SELL
        )



    @property
    def is_filled(
        self,
    ) -> bool:

        return (
            self.status
            ==
            OrderStatus.FILLED
        )



    @property
    def is_cancelled(
        self,
    ) -> bool:

        return (
            self.status
            ==
            OrderStatus.CANCELLED
        )



    @property
    def is_rejected(
        self,
    ) -> bool:

        return (
            self.status
            ==
            OrderStatus.REJECTED
        )



    def _change_status(
        self,
        new_status: OrderStatus,
    ) -> Order:

        OrderStateTransition.validate(
            self.status,
            new_status,
        )


        return Order(
            order_id=self.order_id,
            asset=self.asset,
            side=self.side,
            order_type=self.order_type,
            status=new_status,
            quantity=self.quantity,
            price=self.price,
        )



    def submit(
        self,
    ) -> Order:
        """
        Envia ordem para execução.
        """

        return self._change_status(
            OrderStatus.SUBMITTED,
        )



    def fill(
        self,
    ) -> Order:
        """
        Marca ordem como executada.
        """

        return self._change_status(
            OrderStatus.FILLED,
        )



    def partially_fill(
        self,
    ) -> Order:
        """
        Marca ordem como parcialmente executada.
        """

        return self._change_status(
            OrderStatus.PARTIALLY_FILLED,
        )



    def cancel(
        self,
    ) -> Order:
        """
        Cancela ordem.
        """

        return self._change_status(
            OrderStatus.CANCELLED,
        )



    def reject(
        self,
    ) -> Order:
        """
        Rejeita ordem.
        """

        return self._change_status(
            OrderStatus.REJECTED,
        )
