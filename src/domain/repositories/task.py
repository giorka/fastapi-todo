from abc import ABC

from domain.repositories.base import BaseRepository


class BaseTaskRepository(BaseRepository, ABC):
    ...
