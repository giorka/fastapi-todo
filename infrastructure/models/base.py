from __future__ import annotations

from sqlalchemy.orm.decl_api import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
