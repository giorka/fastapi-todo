from __future__ import annotations

from domain.entities.base import BaseEntity
from domain.repositories.base import BaseRepository
from infrastructure import models
from dataclasses import asdict


class TaskRepository(BaseRepository):
    def add(self, entity: BaseEntity) -> BaseEntity:
        task = models.Task(**asdict(entity))

        self.session.add(task)

        return entity

    def get(self, specification: ...) -> BaseEntity:
        raise NotImplementedError()

    def filter(self, specification: ...) -> list[BaseEntity]:
        raise NotImplementedError()

    def all(self) -> list[BaseEntity]:
        raise NotImplementedError()
