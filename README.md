# Task Manager API

A REST API built with FastAPI, SQLAlchemy and PostgreSQL.

## Stack
- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **Alembic** — database migrations
- **PostgreSQL** — database
- **Docker** — local environment

## Getting started

```bash
# Start database
docker compose up -d

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy env file
cp .env.example .env

# Run the API
uvicorn main:app --reload
```

API docs available at: http://localhost:8000/docs
