# Task API

A simple CRUD API built with FastAPI for managing tasks.

This project was created as part of the FlyRank Backend Internship Week 2 Assignment.

---

## Features

- Create Tasks
- Read All Tasks
- Read Single Task
- Update Tasks
- Delete Tasks
- In-Memory Storage
- Automatic Swagger Documentation

---

## Tech Stack

- Python
- FastAPI
- Uvicorn

---

## Installation

Clone the repository

```bash
git clone <>
```

Move into the project

```bash
cd crud-task-api
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
uvicorn main:app --reload
```

Server:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Single Task |
| POST | /tasks | Create Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

---

## Example curl Request

```bash
curl -i http://127.0.0.1:8000/tasks
```

---

## Swagger UI

Open:

http://127.0.0.1:8000/docs



---

## Author

Sayyam Khalid Satti