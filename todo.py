from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

@todo_router.post("/")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo add successfully"}


@todo_router.get("/todo")
async def retrieve_all_todo() -> dict:
    return {"todos": todo_list}