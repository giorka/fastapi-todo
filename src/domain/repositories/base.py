from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.base import IEntity


@dataclass
class AbstractRepository(ABC):
    session: AsyncSession

    @abstractmethod
    def add(self, entity: IEntity) -> Callable[[], IEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get(self, specification: ...) -> IEntity:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, specification: ...) -> list[IEntity]:
        raise NotImplementedError()

    @abstractmethod
    def all(self) -> list[IEntity]:
        raise NotImplementedError()
