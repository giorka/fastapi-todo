# uvicorn main:app --reload
from dishka import FromDishka, make_async_container
from dishka.integrations.fastapi import inject, setup_dishka
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.task import TaskEntity
from infrastructure.repositories.task import TaskRepository
from ioc import db_provider

app = FastAPI()

container = make_async_container(db_provider)
setup_dishka(container, app)


@app.post('/api/v1/test/')
@inject
async def test(session: FromDishka[AsyncSession]):
    repository = TaskRepository(session)
    repository.add(TaskEntity('тестовая заметка'))
    await session.commit()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
