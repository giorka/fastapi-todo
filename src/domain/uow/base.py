from abc import abstractmethod, ABC

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractUnitOfWork(ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def __exit__(self, *args, **kwargs) -> None:
        self.rollback()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()
