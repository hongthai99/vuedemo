#  ./app/schemas.py
from datetime import datetime
from pydantic import BaseModel


class TodoBase(BaseModel):
    content: str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    done: bool = False
    due: datetime

    class config:
        orm_mode = True
