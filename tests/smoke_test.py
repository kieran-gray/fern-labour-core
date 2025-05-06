from dataclasses import dataclass

from fern_labour_core.aggregate_root import AggregateRoot
from fern_labour_core.entity import Entity
from fern_labour_core.events.event import DomainEvent
from fern_labour_core.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class MockValueObject(ValueObject):
    value: str


@dataclass(eq=False, kw_only=True)
class MockEntity(Entity[MockValueObject]):
    data: str


@dataclass(eq=False, kw_only=True)
class MockAggregateRoot(AggregateRoot[MockValueObject]):
    data: str


class MockConsumer:
    async def start(self) -> None:
        return

    async def stop(self) -> None:
        return

    async def is_healthy(self) -> bool:
        return True


class MockProducer:
    async def publish(self, event: DomainEvent) -> None:
        return

    async def publish_batch(self, events: list[DomainEvent]) -> None:
        return


def can_instantiate_classes() -> None:
    value_object = MockValueObject(value="test")
    MockEntity(id_=value_object, data="test")
    MockAggregateRoot(id_=value_object, data="test")
    MockConsumer()
    MockProducer()
    print("Can instantiate all classes")


if __name__ == "__main__":
    can_instantiate_classes()
