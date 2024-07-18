from abc import abstractmethod

from domain.entities.task import RetrieveTaskEntity, TaskEntity
from domain.repositories.abstract import AbstractRepository


class AbstractTaskRepository(AbstractRepository):
    @abstractmethod
    def add(self, entity: TaskEntity) -> RetrieveTaskEntity:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> list[RetrieveTaskEntity]:
        raise NotImplementedError()
