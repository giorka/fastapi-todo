from domain.entities.base import BaseEntity


class TaskEntity(BaseEntity):
    id: int
    content: str
