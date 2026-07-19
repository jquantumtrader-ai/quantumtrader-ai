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

from app.domain.common.financial_core.orders.query_services import (
    OrderQueryService,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)


def create_order(
    symbol: str,
) -> Order:

    return Order(
        order_id=OrderId(
            uuid4(),
        ),
        asset=Asset(
            symbol,
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


def test_get():

    service = OrderQueryService()

    query = service.get(
        create_order(
            "PETR4",
        ),
    )

    assert query.asset == "PETR4"
    assert query.status == "CREATED"


def test_get_many():

    service = OrderQueryService()

    result = service.get_many(
        [
            create_order(
                "PETR4",
            ),
            create_order(
                "VALE3",
            ),
        ]
    )

    assert len(result) == 2

    assert result[0].asset == "PETR4"

    assert result[1].asset == "VALE3"
