from pymongo import MongoClient  
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

todo_collection = db["todos"]

print(db.list_collection_names())

