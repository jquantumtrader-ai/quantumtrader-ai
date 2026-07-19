from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.common.financial_core.execution.entities import (
    ExecutionEntity,
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


def create_execution():

    return ExecutionEntity.create(
        execution_id=uuid4(),
        order_id=OrderId(
            uuid4(),
        ),
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


def test_execution_entity_creation():

    execution = create_execution()

    assert execution.asset.symbol == "PETR4"
    assert execution.quantity == Decimal(
        "10",
    )


def test_execution_identity():

    execution = create_execution()

    assert execution.is_same_execution(
        execution,
    )


def test_invalid_quantity():

    with pytest.raises(
        ValueError,
    ):

        ExecutionEntity.create(
            execution_id=uuid4(),
            order_id=OrderId(
                uuid4(),
            ),
            asset=Asset(
                "VALE3",
            ),
            quantity=Decimal(
                "0",
            ),
            price=Money(
                "60",
                "BRL",
            ),
        )
