from decimal import Decimal

from app.domain.common.financial_core.value_objects.financial import (
    FinancialValue,
)


def test_financial_value_creation():

    value = FinancialValue("100.123456789")

    assert value.as_decimal() == Decimal(
        "100.123456789"
    )


def test_quantize():

    value = FinancialValue(
        "10.123456789"
    )

    rounded = value.quantize()

    assert rounded.as_decimal() == Decimal(
        "10.12345679"
    )


def test_string_conversion():

    value = FinancialValue("15.75")

    assert value.as_string() == "15.75"


def test_float_conversion():

    value = FinancialValue("20.5")

    assert value.as_float() == 20.5
