# uvicorn main:app --reload
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import APIRouter, FastAPI

from apps.tasks.routes import router as tasks_router
from ioc import db_provider

app = FastAPI()
router = APIRouter(prefix='/api/v1')
router.include_router(tasks_router, prefix='/tasks')
app.include_router(router)

container = make_async_container(db_provider)
setup_dishka(container, app)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
