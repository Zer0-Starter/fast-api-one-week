from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
        cls, 
        item: str = Form(...)
    ): 
        return cls(item=item)

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Wait the next chapter"
            }
        }


class TodoItems(BaseModel):
    todos: list[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1"
                    },
                    {
                        "item": "Example schema 1"
                    }
                ]
            }
        }