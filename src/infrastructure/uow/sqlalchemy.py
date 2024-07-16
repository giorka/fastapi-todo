from domain.uow.base import AsyncAbstractUnitOfWork


class SQLAlchemyUnitOfWork(AsyncAbstractUnitOfWork):
    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
