from sqlalchemy import Column, Integer, String

from infrastructure import models


class TaskModel(models.IModel):
    id = Column(Integer(), primary_key=True)
    content = Column(String(length=255))
