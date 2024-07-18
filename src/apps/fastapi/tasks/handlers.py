from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from domain import entities, services

router = APIRouter(prefix='/tasks')


@router.post('/')
@inject
async def add_task(task: entities.TaskEntity, service: FromDishka[services.TaskService]) -> entities.RetrieveTaskEntity:
    return await service.save(task)
