from dataclasses import dataclass

from domain.entities.base import BaseEntity


@dataclass
class TaskEntity(BaseEntity):
    content: str
