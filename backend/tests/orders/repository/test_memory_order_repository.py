from app.domain.common.financial_core.orders.repository import (
    MemoryOrderRepository,
)


from tests.orders.entities.test_order import (
    create_order,
)



def test_save_and_get():

    repository = MemoryOrderRepository()

    order = create_order()


    repository.save(
        order
    )


    result = repository.get(
        order.order_id
    )


    assert (
        result
        ==
        order
    )



def test_exists():

    repository = MemoryOrderRepository()

    order = create_order()


    repository.save(
        order
    )


    assert (
        repository.exists(
            order.order_id
        )
        is True
    )



def test_delete():

    repository = MemoryOrderRepository()

    order = create_order()


    repository.save(
        order
    )


    repository.delete(
        order.order_id
    )


    assert (
        repository.exists(
            order.order_id
        )
        is False
    )



def test_all():

    repository = MemoryOrderRepository()

    order = create_order()


    repository.save(
        order
    )


    assert (
        len(
            repository.all()
        )
        ==
        1
    )
