from dataclasses import InitVar, dataclass, field
from typing import Generic, TypeVar

from fern_labour_core.entity import Entity
from fern_labour_core.events.event import DomainEvent
from fern_labour_core.value_object import ValueObject

T = TypeVar("T", bound=ValueObject)


@dataclass(eq=False)
class AggregateRoot(Entity[T], Generic[T]):
    """
    Base class for aggregate root entities
    """

    id_: InitVar[T]
    _domain_events: list[DomainEvent] = field(
        default_factory=list, init=False, repr=False, compare=False
    )

    def __post_init__(self, id_: T) -> None:
        super().__init__(id_)

    def add_domain_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def clear_domain_events(self) -> list[DomainEvent]:
        events = self._domain_events.copy()
        self._domain_events.clear()
        return events

    @property
    def domain_events(self) -> list[DomainEvent]:
        return self._domain_events.copy()
