from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.task import TaskEntity
from infrastructure.repositories.task import TaskRepository
from . import schemas

router = APIRouter()


@router.post('/')
@inject
async def add_task(task: schemas.TaskSchema, session: FromDishka[AsyncSession]) -> schemas.TaskSchema:
    repository = TaskRepository(session)
    repository.add(TaskEntity(**dict(task)))
    await session.commit()

    return task
