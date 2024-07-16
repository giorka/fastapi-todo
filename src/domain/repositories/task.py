from abc import ABC

from domain.repositories.base import AbstractRepository


class AbstractTaskRepository(AbstractRepository, ABC):
    ...
