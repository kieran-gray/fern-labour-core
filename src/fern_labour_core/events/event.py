import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Self


@dataclass
class DomainEvent:
    """Base class for all domain events"""

    id: str
    type: str
    aggregate_id: str
    aggregate_type: str
    data: dict[str, Any]
    time: datetime

    @classmethod
    def create(
        cls, aggregate_id: str, aggregate_type: str, data: dict[str, Any], event_type: str = ""
    ) -> Self:
        return cls(
            id=str(uuid.uuid4()),
            type=event_type,
            aggregate_id=aggregate_id,
            aggregate_type=aggregate_type,
            data=data,
            time=datetime.now(UTC),
        )

    @classmethod
    def from_dict(cls, event: dict[str, Any]) -> Self:
        return cls(
            id=event["id"],
            type=event["type"],
            aggregate_id=event["aggregate_id"],
            aggregate_type=event["aggregate_type"],
            data=event["data"],
            time=datetime.fromisoformat(event["time"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "aggregate_id": self.aggregate_id,
            "aggregate_type": self.aggregate_type,
            "data": self.data,
            "time": self.time.isoformat(),
        }
