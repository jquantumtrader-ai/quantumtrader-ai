from decimal import Decimal

import pytest

from app.domain.common.financial_core.exceptions import (
    InvalidOperationException,
)
from app.domain.common.financial_core.value_objects.numeric import (
    NumericValue,
)


def test_numeric_value_creation():

    value = NumericValue("100.50")

    assert value.value == Decimal("100.50")


def test_addition():

    a = NumericValue("10")
    b = NumericValue("5")

    result = a + b

    assert result.value == Decimal("15")


def test_subtraction():

    a = NumericValue("10")
    b = NumericValue("5")

    result = a - b

    assert result.value == Decimal("5")


def test_multiplication():

    a = NumericValue("10")
    b = NumericValue("5")

    result = a * b

    assert result.value == Decimal("50")


def test_division():

    a = NumericValue("10")
    b = NumericValue("5")

    result = a / b

    assert result.value == Decimal("2")


def test_division_by_zero():

    a = NumericValue("10")
    b = NumericValue("0")

    with pytest.raises(
        InvalidOperationException
    ):

        a / b


def test_equality():

    a = NumericValue("100")
    b = NumericValue("100")

    assert a == b


def test_is_immutable():

    value = NumericValue("100")

    with pytest.raises(AttributeError):

        value.value = Decimal("200")


def test_float_is_not_allowed():

    with pytest.raises(TypeError):

        NumericValue(10.5)
