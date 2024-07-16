from __future__ import annotations

from dataclasses import asdict

from domain.entities.base import BaseEntity
from domain.entities.lazy import LazyEntity
from domain.entities.task import CreateTaskEntity
from domain.repositories.task import BaseTaskRepository
# TODO: optimize imports
from infrastructure import models


class TaskRepository(BaseTaskRepository):
    def add(self, entity: BaseEntity) -> LazyEntity:
        entity_dict = asdict(entity)
        task = models.Task(**entity_dict)

        self.session.add(task)

        return LazyEntity(data_source=task.__dict__)

    def get(self, specification: ...) -> CreateTaskEntity:
        raise NotImplementedError()

    def filter(self, specification: ...) -> list[CreateTaskEntity]:
        raise NotImplementedError()

    def all(self) -> list[CreateTaskEntity]:
        raise NotImplementedError()
