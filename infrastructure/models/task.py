from sqlalchemy import Column, Integer, String

from infrastructure.models.base import Base


class Task(Base):
    table_name = 'task'

    id = Column(Integer, primary_key=True)
    content = Column(String(length=255))
