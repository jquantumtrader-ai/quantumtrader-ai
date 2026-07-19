from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.orders import (
    OrderId,
)

from app.domain.common.financial_core.orders.entities import (
    Order,
)

from app.domain.common.financial_core.orders.enums import (
    OrderSide,
    OrderStatus,
    OrderType,
)

from app.domain.common.financial_core.orders.queries import (
    OrderQueryModel,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)


def test_create_query_model():

    order = Order(
        order_id=OrderId(
            uuid4(),
        ),
        asset=Asset(
            "PETR4",
        ),
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        status=OrderStatus.CREATED,
        quantity=Decimal(
            "10",
        ),
        price=Money(
            "30",
            "BRL",
        ),
    )

    query = OrderQueryModel.from_order(
        order,
    )

    assert (
        query.asset
        ==
        "PETR4"
    )

    assert (
        query.status
        ==
        "CREATED"
    )

    assert (
        query.quantity
        ==
        Decimal("10")
    )

    assert (
        query.price
        ==
        Decimal("30")
    )

    assert (
        query.fills
        ==
        0
    )
