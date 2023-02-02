from sqlalchemy import Column, ForeignKey, String, DateTime, Text, Integer
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base

class Campus(Base):
    __tablename__ = "campus"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String(50))
    rank = Column(Integer)