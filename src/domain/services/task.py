from dataclasses import dataclass

from domain.entities.task import RetrieveTaskEntity, TaskEntity
from domain.repositories.task import AbstractTaskRepository
from domain.uow import AsyncUnitOfWork


@dataclass
class TaskService:
    _repository: AbstractTaskRepository
    _uow: AsyncUnitOfWork

    async def save(self, entity: TaskEntity) -> RetrieveTaskEntity:
        entity = self._repository.add(entity)

        await self._uow.commit()

        return entity

    async def all(self) -> list[RetrieveTaskEntity]:
        return await self._repository.all()
