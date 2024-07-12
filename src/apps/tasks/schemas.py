from pydantic import BaseModel, constr


class TaskSchema(BaseModel):
    content: constr(max_length=256)
