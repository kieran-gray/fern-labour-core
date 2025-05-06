from fern_labour_core.events.consumer import EventConsumer


class MockConsumer:
    async def start(self) -> None:
        return

    async def stop(self) -> None:
        return

    async def is_healthy(self) -> bool:
        return True


def test_implementation_is_subclass() -> None:
    assert issubclass(MockConsumer, EventConsumer)
