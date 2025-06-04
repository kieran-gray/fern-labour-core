from datetime import UTC, datetime

import pytest

from fern_labour_core.events.event import DomainEvent
from fern_labour_core.exceptions.domain import DomainError
from tests.conftest import SampleAggregateRoot, SingleFieldValueObject


def test_aggregate_root_id_invariance(sample_aggregate_root: SampleAggregateRoot) -> None:
    with pytest.raises(DomainError):
        sample_aggregate_root.id_ = SingleFieldValueObject(value=123)


def test_aggregate_root_has_domain_events(sample_aggregate_root: SampleAggregateRoot) -> None:
    assert hasattr(sample_aggregate_root, "_domain_events")
    assert sample_aggregate_root._domain_events == []


def test_aggregate_root_add_domain_event(sample_aggregate_root: SampleAggregateRoot) -> None:
    assert sample_aggregate_root._domain_events == []
    domain_event = DomainEvent(
        id="id123",
        type="test.event",
        aggregate_id="test123",
        aggregate_type="agg",
        data={"test": "data", "also": 123},
        time=datetime.now(UTC),
    )
    sample_aggregate_root.add_domain_event(domain_event)
    assert sample_aggregate_root.domain_events == [domain_event]


def test_aggregate_root_clear_domain_events(sample_aggregate_root: SampleAggregateRoot) -> None:
    domain_event = DomainEvent(
        id="id123",
        type="test.event",
        aggregate_id="test123",
        aggregate_type="agg",
        data={"test": "data", "also": 123},
        time=datetime.now(UTC),
    )
    sample_aggregate_root.add_domain_event(domain_event)
    assert sample_aggregate_root.domain_events == [domain_event]

    assert sample_aggregate_root.clear_domain_events() == [domain_event]
    assert sample_aggregate_root.domain_events == []
