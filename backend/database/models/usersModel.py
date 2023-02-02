from sqlalchemy import Column, ForeignKey, String, DateTime, Text, Integer
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    uname = Column(String(50))
    dname = Column(String(50))
    email = Column(String(50))
    github = Column(String(50))
    rank = Column(Integer)
    campus_id = Column(UUID(as_uuid=True), ForeignKey("campus.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
