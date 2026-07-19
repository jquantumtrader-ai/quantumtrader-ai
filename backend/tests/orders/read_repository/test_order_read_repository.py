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

from app.domain.common.financial_core.orders.read_repository import (
    OrderReadRepository,
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


def test_save_and_get():

    repository = OrderReadRepository()

    query = create_query()

    repository.save(
        query,
    )

    loaded = repository.get(
        query.order_id,
    )

    assert loaded is not None
    assert loaded.order_id == query.order_id
    assert loaded.asset == "PETR4"


def test_exists():

    repository = OrderReadRepository()

    query = create_query()

    repository.save(
        query,
    )

    assert repository.exists(
        query.order_id,
    )


def test_count():

    repository = OrderReadRepository()

    repository.save(
        create_query(),
    )

    repository.save(
        create_query(),
    )

    assert repository.count() == 2


def test_clear():

    repository = OrderReadRepository()

    repository.save(
        create_query(),
    )

    repository.clear()

    assert repository.count() == 0


def test_list_all():

    repository = OrderReadRepository()

    repository.save(
        create_query(),
    )

    repository.save(
        create_query(),
    )

    assert len(
        repository.list_all(),
    ) == 2
