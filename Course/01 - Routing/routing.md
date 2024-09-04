# FastAPI

## Routing

Routing is the process of handling HTTP requests. Here, it's manage by *APIRouter*

To create a path operation, we must import *APIRouter* class from fastapi packaage with this code:

```python
from fastapi import APIRouter

todo_router = APIRouter()
```

After that, in our development environment, we'll create a temporary in-app database.

## Pydantic models

It's necessary to have models in our application to ensure only defined data is received or parsed. When defined, modelsa are used as type hints for request body object and request-response objects. [View](`model.py`)

Pydantic models can be nested:

```python
class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item
```

## Path and Query parameters
### Path
The path parameters are used to identify resources.

### Query
The query parameter is used to filter request and return specific data based on the queries supplied