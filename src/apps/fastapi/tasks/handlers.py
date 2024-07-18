from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from domain import entities, services

router = APIRouter(prefix='/tasks')


@router.post('/')
@inject
async def add_task(task: entities.TaskEntity, service: FromDishka[services.TaskService]) -> entities.RetrieveTaskEntity:
    return await service.save(task)


@router.get('/')
@inject
async def get_tasks(service: FromDishka[services.TaskService]) -> list[entities.RetrieveTaskEntity]:
    return await service.all()
