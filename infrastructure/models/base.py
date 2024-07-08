from __future__ import annotations

from sqlalchemy.orm.decl_api import DeclarativeBase, declared_attr

from utils.to_snake_case import to_snake_case


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return to_snake_case(self.__name__)
