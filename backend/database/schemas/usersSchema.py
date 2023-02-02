from uuid import UUID

from pydantic import BaseModel, Field
from datetime import datetime

class UserRequest(BaseModel):
    uname: str
    dname: str
    email: str
    rank: int = 0
    created_at: datetime

class UserResponse(BaseModel):
    id: UUID
    uname: str
    dname: str
    email: str
    github: str
    rank: int
    campus_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True