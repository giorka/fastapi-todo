from sqlalchemy import Column, Integer, String

from infrastructure.models.base import Base


class Task(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String(length=255))
