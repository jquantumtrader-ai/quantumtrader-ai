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

from app.domain.common.financial_core.orders.query_services import (
    OrderQueryService,
)

from app.domain.common.financial_core.orders.read_store import (
    OrderReadStore,
)

from app.domain.common.financial_core.orders.snapshot import (
    OrderSnapshot,
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


def test_complete_order_flow():

    order = create_order()

    store = OrderReadStore()

    projection = OrderProjection(
        read_store=store,
    )

    projection.project(
        order,
    )

    query_service = OrderQueryService()

    result = query_service.get(
        order,
    )

    assert result is not None
    assert result.asset == "PETR4"

    stored = store.read(
        str(
            order.order_id,
        ),
    )

    assert stored is not None


def test_snapshot_restore_flow():

    order = create_order()

    snapshot = OrderSnapshot.from_order(
        order,
    )

    restored = snapshot.restore()

    assert restored.order_id == order.order_id
    assert restored.asset == order.asset
    assert restored.status == order.status
