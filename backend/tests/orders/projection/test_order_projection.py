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

from app.domain.common.financial_core.orders.projection import (
    OrderProjection,
)

from app.domain.common.financial_core.orders.read_store import (
    OrderReadStore,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)


def create_order() -> Order:

    return Order(
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


def test_project():

    store = OrderReadStore()

    projection = OrderProjection(
        read_store=store,
    )

    order = create_order()

    query = projection.project(
        order,
    )

    loaded = store.read(
        query.order_id,
    )

    assert loaded is not None
    assert loaded.asset == "PETR4"
    assert store.count() == 1


def test_remove_projection():

    store = OrderReadStore()

    projection = OrderProjection(
        read_store=store,
    )

    order = create_order()

    query = projection.project(
        order,
    )

    projection.remove(
        query.order_id,
    )

    assert store.count() == 0
