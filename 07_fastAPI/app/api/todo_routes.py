from fastapi import APIRouter
from app.schemas.todo_schema import TodoCreate, TodoUpdate
from app.services.todo_service import (
    create_todo_service,
    get_todos_service,
    update_todo_service,
    delete_todo_service,
    mark_complete_service
)

router = APIRouter()


@router.post("/todos")
def create(todo: TodoCreate):
    return {"id": create_todo_service(todo)}


@router.get("/todos")
def read_all():
    return get_todos_service()


@router.put("/todos/{todo_id}")
def update(todo_id: str, data: TodoUpdate):
    return {"updated": update_todo_service(todo_id, data.dict(exclude_unset=True))}


@router.delete("/todos/{todo_id}")
def delete(todo_id: str):
    return {"deleted": delete_todo_service(todo_id)}


@router.patch("/todos/{todo_id}/complete")
def complete(todo_id: str):
    return {"completed": mark_complete_service(todo_id)}