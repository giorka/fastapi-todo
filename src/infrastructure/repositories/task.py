from sqlalchemy.future import select

from domain import entities
from domain.repositories import AbstractTaskRepository
from infrastructure import datamappers, models, repositories


class TaskRepository(repositories.SQLRepository, AbstractTaskRepository):
    def add(self, entity: entities.TaskEntity) -> entities.RetrieveTaskEntity:
        task_model = datamappers.task.entity_to_model(entity)

        self.session.add(task_model)
        self.session.flush()

        return datamappers.task.model_to_entity(task_model)

    async def all(self) -> list[entities.RetrieveTaskEntity]:
        task_models = await self.session.scalars(select(models.TaskModel))

        return [
            datamappers.task.model_to_entity(task_model)
            for task_model in task_models
        ]
