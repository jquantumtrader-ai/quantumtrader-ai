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

from app.domain.common.financial_core.orders.read_store import (
    OrderReadStore,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)


def create_query() -> OrderQueryModel:

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

    return OrderQueryModel.from_order(
        order,
    )


def test_write_and_read():

    store = OrderReadStore()

    query = create_query()

    store.write(
        query,
    )

    loaded = store.read(
        query.order_id,
    )

    assert loaded is not None
    assert loaded.order_id == query.order_id


def test_count():

    store = OrderReadStore()

    store.write(
        create_query(),
    )

    store.write(
        create_query(),
    )

    assert store.count() == 2


def test_delete():

    store = OrderReadStore()

    query = create_query()

    store.write(
        query,
    )

    store.delete(
        query.order_id,
    )

    assert store.count() == 0


def test_clear():

    store = OrderReadStore()

    store.write(
        create_query(),
    )

    store.write(
        create_query(),
    )

    store.clear()

    assert store.count() == 0


def test_read_all():

    store = OrderReadStore()

    store.write(
        create_query(),
    )

    store.write(
        create_query(),
    )

    assert len(
        store.read_all(),
    ) == 2
