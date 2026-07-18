from decimal import Decimal


from app.domain.common.financial_core.orders.handlers import (
    OrderCommandHandler,
)


from app.domain.common.financial_core.orders.commands import (
    CreateOrderCommand,
)


from app.domain.common.financial_core.orders.enums import (
    OrderSide,
    OrderType,
)


from app.domain.common.financial_core.portfolio.assets.asset import (
    Asset,
)


from app.domain.common.financial_core.value_objects.money import (
    Money,
)



def test_create_command_handler():

    handler = OrderCommandHandler()


    command = CreateOrderCommand(
        asset=Asset(
            "PETR4",
        ),
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=Decimal(
            "10",
        ),
        price=Money(
            "30",
            "BRL",
        ),
    )


    aggregate = handler.handle_create(
        command,
    )


    assert (
        aggregate.order.quantity
        ==
        Decimal("10")
    )


    assert (
        aggregate.order.status.value
        ==
        "CREATED"
    )
