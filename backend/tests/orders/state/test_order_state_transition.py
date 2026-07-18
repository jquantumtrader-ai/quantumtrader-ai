import pytest

from app.domain.common.financial_core.orders.enums import (
    OrderStatus,
)

from app.domain.common.financial_core.orders.state import (
    InvalidOrderTransition,
    OrderStateTransition,
)



def test_created_to_submitted():

    assert (
        OrderStateTransition.can_transition(
            OrderStatus.CREATED,
            OrderStatus.SUBMITTED,
        )
        is True
    )



def test_submitted_to_filled():

    assert (
        OrderStateTransition.can_transition(
            OrderStatus.SUBMITTED,
            OrderStatus.FILLED,
        )
        is True
    )



def test_filled_cannot_return():

    assert (
        OrderStateTransition.can_transition(
            OrderStatus.FILLED,
            OrderStatus.SUBMITTED,
        )
        is False
    )



def test_cancelled_cannot_fill():

    with pytest.raises(
        InvalidOrderTransition,
    ):

        OrderStateTransition.validate(
            OrderStatus.CANCELLED,
            OrderStatus.FILLED,
        )



def test_rejected_is_terminal():

    assert (
        OrderStateTransition.can_transition(
            OrderStatus.REJECTED,
            OrderStatus.SUBMITTED,
        )
        is False
    )
