from abc import abstractmethod

from domain import entities, repositories


class AbstractTaskRepository(repositories.AbstractRepository):
    @abstractmethod
    def add(self, entity: entities.TaskEntity) -> entities.RetrieveTaskEntity:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> list[entities.RetrieveTaskEntity]:
        raise NotImplementedError()
