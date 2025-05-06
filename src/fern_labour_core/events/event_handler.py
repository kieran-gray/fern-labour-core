from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class EventHandler(Protocol):
    """Protocol for event handlers"""

    async def handle(self, event: dict[str, Any]) -> None:
        """Handle the event."""
