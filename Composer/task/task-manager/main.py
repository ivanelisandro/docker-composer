import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from pymongo import MongoClient, errors
from bson.objectid import ObjectId

app = FastAPI()

# Get MongoDB connection parameters
required_env_vars = ['MONGO_HOST_NAME', 'MONGO_PORT_NUMBER', 'MONGO_INITDB_ROOT_USERNAME', 'MONGO_INITDB_ROOT_PASSWORD']
env_vars = {}

# Retrieve environment variables with error handling
for var in required_env_vars:
    try:
        value = os.environ[var]
        if not value:
            raise ValueError(f"Environment variable '{var}' is empty")
        env_vars[var] = value
    except KeyError:
        raise RuntimeError(f"Environment variable '{var}' is not set")
    except Exception as e:
        raise RuntimeError(f"Error retrieving environment variable '{var}': {e}")

host = env_vars['MONGO_HOST_NAME']
mongo_port_number = env_vars['MONGO_PORT_NUMBER']
username = env_vars['MONGO_INITDB_ROOT_USERNAME']
password = env_vars['MONGO_INITDB_ROOT_PASSWORD']

try:
    mongo_port_number = int(mongo_port_number)
except ValueError:
    raise RuntimeError("MongoDB port number must be an integer.")

# Create a MongoClient for DB operations
try:
    client = MongoClient(host,
                         mongo_port_number,
                         username=username,
                         password=password,
                         serverSelectionTimeoutMS=5000)
    client.server_info()  # Trigger a check if it's successful
except errors.ServerSelectionTimeoutError as e:
    raise RuntimeError(f"Failed to connect to MongoDB: {e}")

# Define DB and collection
db = client["task_manager"]
tasks_collection = db["tasks"]


class Task(BaseModel):
    title: str
    description: str


@app.post("/tasks")
def create_task(task: Task):
    try:
        task_dict = task.dict()
        task_id = tasks_collection.insert_one(task_dict).inserted_id
        task_dict["_id"] = str(task_id)
        return task_dict
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error while creating task: {e}")


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: str):
    try:
        task = tasks_collection.find_one({"_id": ObjectId(task_id)})
        if task:
            task["_id"] = str(task["_id"])
            return task
        raise HTTPException(status_code=404, detail=f"Task with id: {task_id} not found.")
    except errors.InvalidId as e:
        raise HTTPException(status_code=400, detail=f"Invalid task ID format: {e}")
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error while retrieving task: {e}")


@app.get("/tasks/title/{task_title}")
def get_task_by_title(task_title: str):
    try:
        task = tasks_collection.find_one({"title": task_title})
        if task:
            task["_id"] = str(task["_id"])
            return task
        raise HTTPException(status_code=404, detail=f"Task with title: {task_title} not found.")
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error while retrieving task: {e}")


@app.get("/tasks")
def get_all_tasks():
    try:
        tasks = tasks_collection.find()
        result = []
        for task in tasks:
            task["_id"] = str(task["_id"])
            result.append(task)
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error while retrieving tasks: {e}")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    try:
        result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count:
            return {"message": "Task has been deleted successfully!"}
        raise HTTPException(status_code=404, detail=f"Task with id: {task_id} not found.")
    except errors.InvalidId as e:
        raise HTTPException(status_code=400, detail=f"Invalid task ID format: {e}")
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error while deleting task: {e}")
