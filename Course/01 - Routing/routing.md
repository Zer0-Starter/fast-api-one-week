# FastAPI

## Routing

    Routing is the process of handling HTTP requests. Here, it's manage by *APIRouter*

    To create a path operation, we must import *APIRouter* class from fastapi packaage with this code:

    ```python
    from fastapi import APIRouter

    todo_router = APIRouter()
    ```

    After that, in our development environment, we'll create a temporary in-app database.
