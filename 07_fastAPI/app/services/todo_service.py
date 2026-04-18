from app.repositories.todo_repo import (
    create_todo, get_todos,
    update_todo, delete_todo, mark_complete
)


def create_todo_service(todo):
    return create_todo(todo)


def get_todos_service():
    return get_todos()


def update_todo_service(todo_id, data):
    return update_todo(todo_id, data)


def delete_todo_service(todo_id):
    return delete_todo(todo_id)


def mark_complete_service(todo_id):
    return mark_complete(todo_id)