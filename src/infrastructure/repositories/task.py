from __future__ import annotations

from domain.entities.builder import GetEntityBuilder
from domain.entities.task import TaskEntity, RetrieveTaskEntity
from domain.repositories.task import AbstractTaskRepository
from infrastructure import models
from infrastructure.repositories.base import SQLRepository


class TaskRepository(SQLRepository, AbstractTaskRepository):
    def add(self, entity: TaskEntity) -> GetEntityBuilder:
        task = models.Task(**entity.dict())

        self.session.add(task)

        return GetEntityBuilder(RetrieveTaskEntity, data_src=task.__dict__)
