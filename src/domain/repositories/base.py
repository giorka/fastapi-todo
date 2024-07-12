from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.base import BaseEntity


@dataclass
class BaseRepository(ABC):
    session: AsyncSession

    @abstractmethod
    def add(self, entity: BaseEntity) -> BaseEntity:
        raise NotImplementedError()

    @abstractmethod
    def get(self, specification: ...) -> BaseEntity:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, specification: ...) -> list[BaseEntity]:
        raise NotImplementedError()

    @abstractmethod
    def all(self) -> list[BaseEntity]:
        raise NotImplementedError()
