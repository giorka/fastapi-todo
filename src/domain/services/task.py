from dataclasses import dataclass

from domain import entities, repositories
from domain.uow import AsyncUnitOfWork


@dataclass
class TaskService:
    _repository: repositories.AbstractTaskRepository
    _uow: AsyncUnitOfWork

    async def save(self, entity: entities.TaskEntity) -> entities.RetrieveTaskEntity:
        entity = self._repository.add(entity)

        await self._uow.commit()

        return entity

    async def all(self) -> list[entities.RetrieveTaskEntity]:
        return await self._repository.all()
