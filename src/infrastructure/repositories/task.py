from sqlalchemy.future import select

from domain.entities.task import TaskEntity, RetrieveTaskEntity
from domain.repositories.task import AbstractTaskRepository
from infrastructure import datamappers
from infrastructure import models
from infrastructure.repositories.base import SQLRepository


class TaskRepository(SQLRepository, AbstractTaskRepository):
    def add(self, entity: TaskEntity) -> RetrieveTaskEntity:
        task_model = datamappers.task.entity_to_model(entity)

        self.session.add(task_model)
        self.session.flush()

        return datamappers.task.model_to_entity(task_model)

    async def all(self) -> list[RetrieveTaskEntity]:
        task_models = await self.session.scalars(select(models.TaskModel))

        return [
            datamappers.task.model_to_entity(task_model)
            for task_model in task_models
        ]
