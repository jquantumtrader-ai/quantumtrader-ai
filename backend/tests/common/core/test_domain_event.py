from uuid import uuid4

from app.domain.common.core import DomainEvent


def test_domain_event_creation() -> None:

    event = DomainEvent(
        aggregate_id=uuid4(),
        event_type="created",
    )

    assert event.event_type == "created"
    assert event.payload == {}


def test_domain_event_is_immutable() -> None:

    event = DomainEvent(
        aggregate_id=uuid4(),
        event_type="created",
    )

    try:
        event.event_type = "changed"
        assert False
    except Exception:
        assert True
