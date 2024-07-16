from pydantic import BaseModel, constr


class CreateTaskSchema(BaseModel):
    content: constr(max_length=256)


class RetrieveTaskSchema(CreateTaskSchema):
    id: int
