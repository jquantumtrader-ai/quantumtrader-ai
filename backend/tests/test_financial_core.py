from decimal import Decimal

from app.domain.common.financial_core.decimal_config import (
    to_decimal,
)


def test_decimal_conversion():

    value = to_decimal("100.50")

    assert value == Decimal("100.50")


def test_float_is_blocked():

    try:

        to_decimal(10.5)

        assert False

    except TypeError:

        assert True
