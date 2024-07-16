from domain.entities.base import IEntity
from domain.entities.mixins.id import IDFieldMixin


class TaskEntity(IEntity):
    content: str


class RetrieveTaskEntity(TaskEntity, IDFieldMixin):
    id: int
