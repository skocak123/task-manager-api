from fastapi import FastAPI
from app.models import User, Project, Task
from app.routers import auth, projects, tasks

app = FastAPI(
    title="Task Manager API",
    version="0.1.0",
    swagger_ui_parameters={"persistAuthorization": True},
)

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
