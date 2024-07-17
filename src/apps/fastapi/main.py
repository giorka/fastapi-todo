import uvicorn
from fastapi import FastAPI, APIRouter

from config import settings
from .tasks import router as tasks_router

routers: list[APIRouter] = [
    tasks_router,
]


def get_application() -> FastAPI:
    application = FastAPI()
    api_router = APIRouter(prefix='/api')

    for router in routers:
        api_router.include_router(router)

    application.include_router(api_router)

    return application


def get_server(application: FastAPI) -> uvicorn.Server:
    server = uvicorn.Server(
        uvicorn.Config(
            app=application,
            host='0.0.0.0',
            port=7000,
            reload=settings.debug
        )
    )

    return server
