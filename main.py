from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks built with FastAPI.",
    version="1.0.0"
)

class TaskCreate(BaseModel):
    title: str
class TaskUpdate(BaseModel):
    title: str
    done: bool
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "done": False
    },
    {
        "id": 3,
        "title": "Push to GitHub",
        "done": False
    }
]


@app.get(
    "/",
    summary="API Information",
    description="Returns basic information about the Task API."
)
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


@app.get(
    "/health",
    summary="Health Check",
    description="Checks whether the API is running."
)
def health():
    return {
        "status": "ok"
    }
    
@app.get(
    "/tasks",
    summary="Get All Tasks",
    description="Returns all tasks stored in memory."
)
def get_tasks():
    return tasks


@app.get(
    "/tasks/{task_id}",
    summary="Get Task By ID",
    description="Returns a single task using its ID."
)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )
    
@app.post(
    "/tasks",
    status_code=201,
    summary="Create Task",
    description="Creates a new task."
)
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put(
    "/tasks/{task_id}",
    summary="Update Task",
    description="Updates an existing task."
)
def update_task(task_id: int, updated_task: TaskUpdate):

    if not updated_task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["done"] = updated_task.done
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    summary="Delete Task",
    description="Deletes a task by its ID."
)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return Response(status_code=204)

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )