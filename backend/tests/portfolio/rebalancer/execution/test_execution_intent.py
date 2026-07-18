from decimal import Decimal

import pytest

from app.domain.common.financial_core.portfolio.rebalancer.execution import (
    ExecutionIntent,
    IntentType,
)


def test_buy_intent():

    class Action:

        quantity_difference = Decimal(
            "5"
        )


    intent = ExecutionIntent.from_action(
        Action()
    )

    assert intent.intent_type == IntentType.BUY

    assert intent.quantity == Decimal(
        "5"
    )



def test_sell_intent():

    class Action:

        quantity_difference = Decimal(
            "-2"
        )


    intent = ExecutionIntent.from_action(
        Action()
    )

    assert intent.intent_type == IntentType.SELL

    assert intent.quantity == Decimal(
        "2"
    )



def test_hold_intent():

    class Action:

        quantity_difference = Decimal(
            "0"
        )


    intent = ExecutionIntent.from_action(
        Action()
    )

    assert intent.intent_type == IntentType.HOLD

    assert intent.quantity == Decimal(
        "0"
    )



def test_negative_quantity_not_allowed():

    with pytest.raises(
        ValueError
    ):

        class Action:

            quantity_difference = Decimal(
                "-1"
            )


        ExecutionIntent(
            action=Action(),
            intent_type=IntentType.BUY,
            quantity=Decimal("-1"),
        )
