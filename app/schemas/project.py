from pydantic import BaseModel
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    created_at: datetime

    model_config = {"from_attributes": True}
