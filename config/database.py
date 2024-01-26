from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:v8RcNc2VQL1D5p4m@cluster0.0bx7pop.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collections"]