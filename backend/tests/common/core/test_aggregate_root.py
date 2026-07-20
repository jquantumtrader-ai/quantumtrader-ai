from uuid import uuid4

from app.domain.common.core import AggregateRoot, DomainEvent


class FakeAggregate(AggregateRoot[DomainEvent]):
    pass


def test_record_event() -> None:
    aggregate = FakeAggregate()

    event = DomainEvent(
        aggregate_id=uuid4(),
        event_type="created",
    )

    aggregate.record_event(event)

    assert len(aggregate.events) == 1
    assert int(aggregate.version) == 1


def test_pull_events() -> None:
    aggregate = FakeAggregate()

    aggregate.record_event(
        DomainEvent(
            aggregate_id=uuid4(),
            event_type="created",
        )
    )

    events = aggregate.pull_events()

    assert len(events) == 1
    assert aggregate.events == ()


def test_clear_events() -> None:
    aggregate = FakeAggregate()

    aggregate.record_event(
        DomainEvent(
            aggregate_id=uuid4(),
            event_type="created",
        )
    )

    aggregate.clear_events()

    assert aggregate.events == ()
