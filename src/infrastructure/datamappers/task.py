from domain import entities
from infrastructure import models


def model_to_entity(task_model: models.TaskModel) -> entities.RetrieveTaskEntity:
    return entities.RetrieveTaskEntity(
        id=task_model.id,
        content=task_model.content
    )


def entity_to_model(task_entity: entities.TaskEntity) -> models.TaskModel:
    return models.TaskModel(**task_entity.dict())
