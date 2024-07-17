from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from domain.entities.task import TaskEntity, RetrieveTaskEntity
from domain.services.task import TaskService

router = APIRouter(prefix='/tasks')


@router.post('/')
@inject
async def add_task(task: TaskEntity, service: FromDishka[TaskService]) -> RetrieveTaskEntity:
    return await service.save(task)
