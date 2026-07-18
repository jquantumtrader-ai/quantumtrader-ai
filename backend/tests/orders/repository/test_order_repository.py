from app.domain.common.financial_core.orders.repository import (
    OrderRepository,
)


def test_repository_protocol_exists():

    assert (
        OrderRepository
        is not None
    )
