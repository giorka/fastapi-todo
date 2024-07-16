from dataclasses import dataclass

from domain.entities.base import BaseEntity


@dataclass
class CreateTaskEntity(BaseEntity):
    content: str


@dataclass
class RetrieveTaskEntity(CreateTaskEntity):
    id: int
