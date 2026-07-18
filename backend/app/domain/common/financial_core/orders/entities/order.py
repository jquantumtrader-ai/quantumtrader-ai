from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from ...portfolio.assets.asset import Asset
from ...value_objects.money import Money
from ..enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)
from ..fills import Fill
from ..order_id import OrderId
from ..state import OrderStateTransition



@dataclass(frozen=True)
class Order:
    """
    Representa uma ordem financeira
    com ciclo de vida e controle
    de execuções.
    """


    order_id: OrderId

    asset: Asset

    side: OrderSide

    order_type: OrderType

    status: OrderStatus

    quantity: Decimal

    price: Money

    fills: tuple[Fill, ...] = field(
        default_factory=tuple,
    )



    def __post_init__(self) -> None:

        if self.quantity <= Decimal("0"):

            raise ValueError(
                "Quantidade deve ser maior que zero."
            )



    @property
    def notional(self) -> Money:

        return Money(
            self.quantity
            *
            self.price.value,
            self.price.currency,
        )



    @property
    def executed_quantity(self) -> Decimal:

        return sum(
            (
                fill.quantity
                for fill in self.fills
            ),
            Decimal("0"),
        )



    @property
    def remaining_quantity(self) -> Decimal:

        return (
            self.quantity
            -
            self.executed_quantity
        )



    @property
    def is_filled(self) -> bool:

        return (
            self.status
            ==
            OrderStatus.FILLED
        )



    @property
    def is_cancelled(self) -> bool:

        return (
            self.status
            ==
            OrderStatus.CANCELLED
        )



    @property
    def is_rejected(self) -> bool:

        return (
            self.status
            ==
            OrderStatus.REJECTED
        )



    @property
    def average_execution_price(
        self,
    ) -> Money | None:

        if not self.fills:

            return None


        total_value = sum(
            (
                fill.value.value
                for fill in self.fills
            ),
            Decimal("0"),
        )


        return Money(
            total_value
            /
            self.executed_quantity,
            self.price.currency,
        )



    def add_fill(
        self,
        fill: Fill,
    ) -> Order:


        if (
            fill.order_id
            !=
            self.order_id
        ):

            raise ValueError(
                "Fill pertence a outra ordem."
            )


        if (
            self.executed_quantity
            +
            fill.quantity
            >
            self.quantity
        ):

            raise ValueError(
                "Quantidade executada excede a ordem."
            )


        new_fills = (
            *self.fills,
            fill,
        )


        new_status = self.status


        executed = sum(
            (
                item.quantity
                for item in new_fills
            ),
            Decimal("0"),
        )


        if executed == self.quantity:

            new_status = OrderStatus.FILLED


        elif self.status == OrderStatus.SUBMITTED:

            new_status = OrderStatus.PARTIALLY_FILLED



        return Order(
            order_id=self.order_id,
            asset=self.asset,
            side=self.side,
            order_type=self.order_type,
            status=new_status,
            quantity=self.quantity,
            price=self.price,
            fills=new_fills,
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
            fills=self.fills,
        )



    def submit(self) -> Order:

        return self._change_status(
            OrderStatus.SUBMITTED,
        )



    def fill(self) -> Order:

        return self._change_status(
            OrderStatus.FILLED,
        )



    def partially_fill(self) -> Order:

        return self._change_status(
            OrderStatus.PARTIALLY_FILLED,
        )



    def cancel(self) -> Order:

        return self._change_status(
            OrderStatus.CANCELLED,
        )



    def reject(self) -> Order:

        return self._change_status(
            OrderStatus.REJECTED,
        )
