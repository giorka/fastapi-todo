from sqlalchemy import Column, Integer, String

from infrastructure.models.base import IModel


class TaskModel(IModel):
    id = Column(Integer(), primary_key=True)
    content = Column(String(length=255))
