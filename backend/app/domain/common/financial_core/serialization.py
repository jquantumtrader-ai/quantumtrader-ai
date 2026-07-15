from decimal import Decimal


def serialize_value(value):

    if isinstance(value, Decimal):
        return str(value)

    return value
