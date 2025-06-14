import logging
from types import TracebackType
from typing import Self

import pytest

from fern_labour_core.unit_of_work import UnitOfWork

log = logging.getLogger(__name__)


class MockException(Exception):
    pass


class MockUnitOfWork(UnitOfWork):
    async def __aenter__(self) -> Self:
        log.info("Entering UnitOfWork")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        try:
            if exc_type is not None:
                await self.rollback()
            else:
                await self.commit()
        except Exception:
            log.info("Exception")
        finally:
            log.info("Exiting UnitOfWork")
        return None

    async def commit(self) -> None:
        log.info("Committing")

    async def rollback(self) -> None:
        log.info("Rolling Back")


async def test_unit_of_work(caplog: pytest.LogCaptureFixture) -> None:
    unit_of_work = MockUnitOfWork()
    with caplog.at_level(logging.INFO):
        async with unit_of_work:
            pass
    assert "Entering UnitOfWork" in caplog.text
    assert "Committing" in caplog.text
    assert "Exiting UnitOfWork" in caplog.text


async def test_unit_of_work_raises(caplog: pytest.LogCaptureFixture) -> None:
    unit_of_work = MockUnitOfWork()
    with caplog.at_level(logging.INFO):
        with pytest.raises(MockException):
            async with unit_of_work:
                raise MockException()
    assert "Entering UnitOfWork" in caplog.text
    assert "Rolling Back" in caplog.text
    assert "Exiting UnitOfWork" in caplog.text
