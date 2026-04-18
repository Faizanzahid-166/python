from fastapi import FastAPI
from app.api.todo_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Todo API is running 🚀"}