import pytest

from app.domain.common.financial_core.currency import (
    BRL,
    USD,
)

from app.domain.common.financial_core.value_objects.money import (
    Money,
)

from app.domain.common.financial_core.value_objects.money_exceptions import (
    CurrencyMismatchError,
)


def test_money_addition():

    first = Money("100", BRL)
    second = Money("50", BRL)

    result = first + second

    assert result.as_string() == "150"
    assert result.currency == BRL


def test_money_subtraction():

    first = Money("100", BRL)
    second = Money("40", BRL)

    result = first - second

    assert result.as_string() == "60"


def test_currency_mismatch():

    brl = Money("100", BRL)
    usd = Money("100", USD)

    with pytest.raises(
        CurrencyMismatchError
    ):
        brl + usd
