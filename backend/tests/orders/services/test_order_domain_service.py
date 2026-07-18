from decimal import Decimal

from app.domain.common.financial_core.orders.services import (
    OrderDomainService,
)

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)

from tests.orders.entities.test_order import (
    create_order,
)



def test_can_execute_created_order():

    service = OrderDomainService()

    order = create_order(
        OrderStatus.CREATED
    )


    assert (
        service.can_execute(
            order
        )
        is True
    )



def test_filled_order_cannot_execute():

    service = OrderDomainService()

    order = create_order(
        OrderStatus.FILLED
    )


    assert (
        service.can_execute(
            order
        )
        is False
    )



def test_cancel_validation():

    service = OrderDomainService()

    order = create_order(
        OrderStatus.CREATED
    )


    assert (
        service.can_cancel(
            order
        )
        is True
    )



def test_filled_order_completed():

    service = OrderDomainService()

    order = create_order(
        OrderStatus.FILLED
    )


    assert (
        service.is_completed(
            order
        )
        is True
    )



def test_remaining_quantity():

    service = OrderDomainService()

    order = create_order()


    assert (
        service.remaining_quantity(
            order
        )
        ==
        Decimal("10")
    )
