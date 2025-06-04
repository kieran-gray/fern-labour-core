from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from fern_labour_core.events.event import DomainEvent


@dataclass
class BatchPublishResult:
    success_ids: list[str]
    failure_ids: list[str]


@runtime_checkable
class EventProducer(Protocol):
    """Protocol for event producers"""

    async def publish(self, event: DomainEvent) -> bool:
        """Publish single event."""

    async def publish_batch(self, events: list[DomainEvent]) -> BatchPublishResult:
        """Publish batch of events."""
