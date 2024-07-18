from abc import abstractmethod

from domain.entities.base import IEntity
from domain.entities.builder import GetEntityBuilder
from domain.repositories.abstract import AbstractRepository


class AbstractTaskRepository(AbstractRepository):
    @abstractmethod
    def add(self, entity: IEntity) -> GetEntityBuilder:
        raise NotImplementedError()
