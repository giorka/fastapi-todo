from __future__ import annotations

from sqlalchemy.orm.decl_api import declarative_base


class BaseMeta(type):
    def __new__(cls, name: str, bases: tuple[type, ...], attrs: dict) -> 'BaseMeta':
        if '__tablename__' not in attrs:
            attrs['__tablename__'] = name.lower()

        return super().__new__(cls, name, bases, attrs)


Base = declarative_base(metaclass=BaseMeta)
