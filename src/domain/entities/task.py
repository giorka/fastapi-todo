from domain import entities


class TaskEntity(entities.IEntity):
    content: str


class RetrieveTaskEntity(TaskEntity, entities.mixins.IDFieldMixin):
    id: int
