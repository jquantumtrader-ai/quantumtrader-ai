from app.domain.common.financial_core.orders.policies import (
    OrderPolicyEngine,
)

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)

from tests.orders.entities.test_order import (
    create_order,
)



def test_policy_can_execute():

    engine = OrderPolicyEngine()


    order = create_order(
        OrderStatus.CREATED
    )


    assert (
        engine.can_execute(
            order
        )
        is True
    )



def test_policy_cannot_execute_filled():

    engine = OrderPolicyEngine()


    order = create_order(
        OrderStatus.FILLED
    )


    assert (
        engine.can_execute(
            order
        )
        is False
    )



def test_policy_can_cancel():

    engine = OrderPolicyEngine()


    order = create_order(
        OrderStatus.CREATED
    )


    assert (
        engine.can_cancel(
            order
        )
        is True
    )



def test_policy_completed():

    engine = OrderPolicyEngine()


    order = create_order(
        OrderStatus.FILLED
    )


    assert (
        engine.is_completed(
            order
        )
        is True
    )
