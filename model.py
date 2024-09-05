from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Wait the next chapter"
            }
        }


class TodoItems(BaseModel):
    todos: list[TodoItem]

    class Config:
        schema_extra = {
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