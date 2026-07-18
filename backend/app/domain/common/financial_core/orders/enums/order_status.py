from __future__ import annotations

from enum import Enum


class OrderStatus(
    str,
    Enum,
):
    """
    Estado atual de uma ordem.
    """

    CREATED = "CREATED"

    SUBMITTED = "SUBMITTED"

    PARTIALLY_FILLED = "PARTIALLY_FILLED"

    FILLED = "FILLED"

    CANCELLED = "CANCELLED"

    REJECTED = "REJECTED"
