# uvicorn main:app --reload
import asyncio

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from apps.fastapi import get_application, get_server
from ioc import DatabaseProvider, RepositoryProvider, ServiceProvider


async def main() -> None:
    container = make_async_container(
        DatabaseProvider(),
        RepositoryProvider(),
        ServiceProvider()
    )

    application = get_application()

    setup_dishka(container, application)

    await get_server(application).serve()


if __name__ == '__main__':
    asyncio.run(main())
