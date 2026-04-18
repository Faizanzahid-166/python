from bson import ObjectId
from app.db.mongodb import todo_collection


# ✅ CREATE
def create_todo(todo):
    data = {
        "title": todo.title,
        "description": todo.description,
        "completed": False
    }
    result = todo_collection.insert_one(data)
    return str(result.inserted_id)


# ✅ READ
def get_todos():
    todos = []
    for t in todo_collection.find():
        todos.append({
            "id": str(t["_id"]),
            "title": t["title"],
            "description": t.get("description"),
            "completed": t["completed"]
        })
    return todos


# ✏️ UPDATE
def update_todo(todo_id, data):
    result = todo_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": data}
    )
    return result.modified_count


# ❌ DELETE
def delete_todo(todo_id):
    result = todo_collection.delete_one(
        {"_id": ObjectId(todo_id)}
    )
    return result.deleted_count


# ✅ MARK COMPLETE
def mark_complete(todo_id):
    result = todo_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": {"completed": True}}
    )
    return result.modified_count