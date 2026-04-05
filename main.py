from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference
from app.routers import auth, projects, tasks

app = FastAPI(title="Task Manager API", version="0.1.0", docs_url=None)

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/docs", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url="/openapi.json",
        title="Task Manager API",
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}
