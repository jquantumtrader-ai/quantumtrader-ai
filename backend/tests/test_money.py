from app.domain.common.financial_core.currency import BRL
from app.domain.common.financial_core.value_objects.money import Money


def test_money_creation() -> None:
    money = Money("100.50", BRL)

    assert money.currency == BRL
    assert money.as_string() == "100.50"


def test_money_string_representation() -> None:
    money = Money("250", BRL)

    assert str(money) == "BRL 250"
