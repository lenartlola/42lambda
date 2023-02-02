from uuid import UUID

from pydantic import BaseModel, Field
from datetime import datetime

class CampusRequest(BaseModel):
    name: str
    rank: int = 0

class CampusResponse(BaseModel):
    id: UUID
    name: str
    rank: int

    class Config:
        orm_mode = True