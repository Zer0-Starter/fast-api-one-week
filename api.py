from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcom() -> dict:
    return {"message": "Hello world"}

app.include_router(todo_router)