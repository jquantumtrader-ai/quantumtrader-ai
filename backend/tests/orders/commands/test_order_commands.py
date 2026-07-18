from decimal import Decimal
from uuid import uuid4


from app.domain.common.financial_core.orders.commands import (
    CreateOrderCommand,
    CancelOrderCommand,
    FillOrderCommand,
    RejectOrderCommand,
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


from app.domain.common.financial_core.orders.enums import (
    OrderSide,
    OrderType,
)



BRL = "BRL"



def test_create_order_command():

    command = CreateOrderCommand(
        asset=Asset(
            "PETR4"
        ),
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=Decimal("10"),
        price=Money(
            "30",
            BRL
        ),
    )


    assert command.quantity == Decimal("10")



def test_cancel_order_command():

    command = CancelOrderCommand(
        OrderId(
            uuid4()
        )
    )


    assert command.order_id is not None



def test_fill_order_command():

    command = FillOrderCommand(
        OrderId(
            uuid4()
        ),
        Decimal("5"),
        Money(
            "30",
            BRL
        ),
    )


    assert command.quantity == Decimal("5")



def test_reject_order_command():

    command = RejectOrderCommand(
        OrderId(
            uuid4()
        ),
        "Risk limit",
    )


    assert command.reason == "Risk limit"
