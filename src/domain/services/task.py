from domain.entities.base import BaseEntity
from domain.repositories.task import BaseTaskRepository
from domain.uow.base import AbstractUnitOfWork


class TaskService:
    def __init__(self, repository: BaseTaskRepository, uow: AbstractUnitOfWork) -> None:
        self._repository = repository
        self._uow = uow

    async def new_task(self, entity: BaseEntity) -> BaseEntity:
        created_entity = self._repository.add(entity)

        async with self._uow:
            await self._uow.commit()

        return created_entity
