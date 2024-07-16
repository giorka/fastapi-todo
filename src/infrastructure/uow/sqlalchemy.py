from domain.uow.base import AbstractUnitOfWork


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    async def __aenter__(self, *args, **kwargs) -> 'SQLAlchemyUnitOfWork':
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        await self.rollback()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
