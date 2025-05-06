from typing import Protocol, runtime_checkable

from fern_labour_core.events.event import DomainEvent


@runtime_checkable
class EventProducer(Protocol):
    """Protocol for event producers"""

    async def publish(self, event: DomainEvent) -> None:
        """Publish single event."""

    async def publish_batch(self, events: list[DomainEvent]) -> None:
        """Publish batch of events."""
