import pytest

from app.domain.common.financial_core.execution.value_objects import (
    AggregateVersion,
)


def test_default_version() -> None:

    version = AggregateVersion()

    assert int(version) == 0


def test_next_version() -> None:

    version = AggregateVersion(5)

    next_version = version.next()

    assert int(next_version) == 6


def test_negative_version() -> None:

    with pytest.raises(ValueError):

        AggregateVersion(-1)


def test_ordering() -> None:

    assert AggregateVersion(2) > AggregateVersion(1)
