from dataclasses import dataclass

from domain.entities.task import RetrieveTaskEntity, TaskEntity
from domain.uow import AsyncUnitOfWork
from infrastructure.repositories.task import TaskRepository


@dataclass
class TaskService:
    _repository: TaskRepository
    _uow: AsyncUnitOfWork

    async def save(self, entity: TaskEntity) -> RetrieveTaskEntity:
        get_entity = self._repository.add(entity)

        await self._uow.commit()

        return get_entity()
