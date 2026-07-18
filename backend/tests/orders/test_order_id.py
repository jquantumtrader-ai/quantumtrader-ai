from app.domain.common.financial_core.orders import (
    OrderId,
)


def test_create_new_order_id():

    order_id = OrderId.new()

    assert isinstance(
        str(order_id),
        str,
    )

    assert len(
        str(order_id),
    ) == 36


def test_from_string():

    order_id = OrderId.new()

    reconstructed = OrderId.from_string(
        str(order_id),
    )

    assert reconstructed == order_id


def test_two_ids_are_different():

    first = OrderId.new()

    second = OrderId.new()

    assert first != second
