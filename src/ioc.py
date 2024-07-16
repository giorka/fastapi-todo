from typing import AsyncIterable

from dishka import provide, Provider, Scope
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, AsyncSession, create_async_engine

from config import settings
from domain.repositories.task import BaseTaskRepository
from domain.services.task import TaskService
from infrastructure.repositories.task import TaskRepository
from infrastructure.uow.sqlalchemy import SQLAlchemyUnitOfWork


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_engine(self) -> AsyncEngine:
        return create_async_engine(
            settings.db_url,
            echo=False,
            pool_recycle=180
        )

    @provide(scope=Scope.APP)
    def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(self, factory: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        session = factory()

        yield session

        print('log')
        await session.close()


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_task_repository(self, session: AsyncSession) -> BaseTaskRepository:
        return TaskRepository(session)


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_task_service(self, task_repository: BaseTaskRepository) -> TaskService:
        return TaskService(task_repository, SQLAlchemyUnitOfWork(task_repository.session))


db_provider = DatabaseProvider()
repository_provider = RepositoryProvider()
service_provider = ServiceProvider()
