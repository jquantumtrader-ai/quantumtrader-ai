from app.domain.common.financial_core.orders.manager import (
    OrderManager,
)

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)


from tests.orders.entities.test_order import (
    create_order,
)



def test_register_order():

    manager = OrderManager()

    order = create_order()


    manager.register(
        order
    )


    assert (
        manager.exists(
            order.order_id
        )
        is True
    )



def test_get_order():

    manager = OrderManager()

    order = create_order()


    manager.register(
        order
    )


    result = manager.get(
        order.order_id
    )


    assert (
        result
        ==
        order
    )



def test_cancel_order():

    manager = OrderManager()

    order = create_order()


    manager.register(
        order
    )


    cancelled = manager.cancel(
        order.order_id
    )


    assert (
        cancelled.status
        ==
        OrderStatus.CANCELLED
    )



def test_all_orders():

    manager = OrderManager()

    order = create_order()


    manager.register(
        order
    )


    assert (
        len(
            manager.all()
        )
        ==
        1
    )
