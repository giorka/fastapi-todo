from abc import ABC, abstractmethod

from domain.entities.base import IEntity
from domain.entities.builder import GetEntityBuilder
from domain.repositories.base import IRepository


class AbstractTaskRepository(IRepository, ABC):
    @abstractmethod
    def add(self, entity: IEntity) -> GetEntityBuilder:
        raise NotImplementedError()
