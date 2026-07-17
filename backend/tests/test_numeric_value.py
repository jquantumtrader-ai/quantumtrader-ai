from decimal import Decimal

import pytest

from app.domain.common.financial_core.value_objects.numeric import (
    NumericValue,
)


def test_numeric_value_creation() -> None:

    value = NumericValue("100.50")

    assert value.value == Decimal("100.50")


def test_as_decimal() -> None:

    value = NumericValue("42.75")

    assert value.as_decimal() == Decimal("42.75")


def test_equality() -> None:

    a = NumericValue("100")

    b = NumericValue("100")

    assert a == b


def test_inequality() -> None:

    a = NumericValue("100")

    b = NumericValue("101")

    assert a != b


def test_repr() -> None:

    value = NumericValue("10")

    assert repr(value) == "NumericValue(value=10)"


def test_is_immutable() -> None:

    value = NumericValue("100")

    with pytest.raises(AttributeError):

        value.value = Decimal("200")


def test_float_is_not_allowed() -> None:

    with pytest.raises(TypeError):

        NumericValue(10.5)
