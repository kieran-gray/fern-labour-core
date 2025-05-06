from fern_labour_core.events.event import DomainEvent
from fern_labour_core.events.producer import EventProducer


class MockProducer:
    async def publish(self, event: DomainEvent) -> None:
        return

    async def publish_batch(self, events: list[DomainEvent]) -> None:
        return


def test_implementation_is_subclass() -> None:
    assert issubclass(MockProducer, EventProducer)
