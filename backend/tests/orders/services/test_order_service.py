from app.domain.common.financial_core.orders.services import (
    OrderService,
)

from app.domain.common.financial_core.orders.repository import (
    MemoryOrderRepository,
)

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)


from tests.orders.entities.test_order import (
    create_order,
)



def create_service():

    return OrderService(
        MemoryOrderRepository()
    )



def test_create_order():

    service = create_service()

    order = create_order()


    result = service.create(
        order
    )


    assert (
        result
        ==
        order
    )



def test_get_order():

    service = create_service()

    order = create_order()


    service.create(
        order
    )


    result = service.get(
        order.order_id
    )


    assert (
        result
        ==
        order
    )



def test_cancel_order():

    service = create_service()

    order = create_order()


    service.create(
        order
    )


    cancelled = service.cancel(
        order.order_id
    )


    assert (
        cancelled.status
        ==
        OrderStatus.CANCELLED
    )



def test_list_orders():

    service = create_service()

    order = create_order()


    service.create(
        order
    )


    assert (
        len(
            service.list_orders()
        )
        ==
        1
    )
