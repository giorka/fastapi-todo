import os

from pydantic_settings import BaseSettings, SettingsConfigDict

src_path = os.path.dirname(os.path.abspath(__file__))
env_file = os.path.join(src_path, '.env')


class Settings(BaseSettings):
    db_engine: str = ...
    db_name: str = ...
    db_user: str = ...
    db_password: str = ...
    db_host: str = ...
    db_port: str = ...

    model_config = SettingsConfigDict(env_file=env_file)

    @property
    def db_url(self) -> str:
        return '{db_engine}+asyncpg://{db_user}:{db_password}@{db_host}/{db_name}'.format(**self.__dict__)


settings = Settings()
