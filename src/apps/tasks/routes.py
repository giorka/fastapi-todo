from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from domain.entities.task import CreateTaskEntity
from domain.services.task import TaskService
from . import schemas

router = APIRouter()


@router.post('/')
@inject
async def add_task(task: schemas.CreateTaskSchema, service: FromDishka[TaskService]) -> schemas.RetrieveTaskSchema:
    entity = CreateTaskEntity(**dict(task))
    created_task = await service.new_task(entity)

    return schemas.RetrieveTaskSchema(**created_task.__dict__)
