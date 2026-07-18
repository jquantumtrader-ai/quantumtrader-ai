from app.domain.common.financial_core.orders.specifications import (
    OrderCanExecuteSpecification,
    OrderCanCancelSpecification,
    OrderCompletedSpecification,
)

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)

from tests.orders.entities.test_order import (
    create_order,
)



def test_can_execute():

    spec = OrderCanExecuteSpecification()

    order = create_order(
        OrderStatus.CREATED
    )


    assert (
        spec.is_satisfied_by(
            order
        )
        is True
    )



def test_cannot_execute_filled():

    spec = OrderCanExecuteSpecification()

    order = create_order(
        OrderStatus.FILLED
    )


    assert (
        spec.is_satisfied_by(
            order
        )
        is False
    )



def test_can_cancel():

    spec = OrderCanCancelSpecification()

    order = create_order(
        OrderStatus.CREATED
    )


    assert (
        spec.is_satisfied_by(
            order
        )
        is True
    )



def test_completed():

    spec = OrderCompletedSpecification()

    order = create_order(
        OrderStatus.FILLED
    )


    assert (
        spec.is_satisfied_by(
            order
        )
        is True
    )
