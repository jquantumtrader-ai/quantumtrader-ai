from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from app.domain.common.financial_core.execution import (
    Execution,
)

from app.domain.common.financial_core.orders import (
    OrderId,
)

from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)


def test_create_execution():

    order_id = OrderId(
        uuid4(),
    )

    execution = Execution.create(
        execution_id=uuid4(),
        order_id=order_id,
        asset=Asset(
            "PETR4",
        ),
        quantity=Decimal(
            "10",
        ),
        price=Money(
            "30",
            "BRL",
        ),
    )

    assert execution.order_id == order_id
    assert execution.asset.symbol == "PETR4"
    assert execution.quantity == Decimal(
        "10",
    )
    assert execution.price.value == Decimal(
        "30",
    )


def test_execution_timestamp():

    execution = Execution.create(
        execution_id=uuid4(),
        order_id=OrderId(
            uuid4(),
        ),
        asset=Asset(
            "VALE3",
        ),
        quantity=Decimal(
            "5",
        ),
        price=Money(
            "65",
            "BRL",
        ),
    )

    assert isinstance(
        execution.executed_at,
        datetime,
    )
