from abc import ABC
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class AbstractUnitOfWork(ABC):
    _session: AsyncSession

    def commit(self, *args, **kwargs) -> None:
        raise NotImplementedError()

    def rollback(self, *args, **kwargs) -> None:
        raise NotImplementedError()


class AsyncAbstractUnitOfWork(AbstractUnitOfWork):
    async def commit(self, *args, **kwargs) -> None:
        raise NotImplementedError()

    async def rollback(self, *args, **kwargs) -> None:
        raise NotImplementedError()
