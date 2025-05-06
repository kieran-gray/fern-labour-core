from typing import Any

from fern_labour_core.events.event_handler import EventHandler


class MockEventHandler:
    def handle(self, event: dict[str, Any]) -> None:
        return None


def test_implementation_is_subclass() -> None:
    assert issubclass(MockEventHandler, EventHandler)
