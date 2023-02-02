import uuid
from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database.models.usersModel import User
from database.models.campusModel import Campus

def get_campus(db: Session, campus_name: str):
    campus = db.query(Campus).filter(Campus.name == campus_name).first()
    if not campus:
        return None
    return campus

def create_campus(db: Session, campus: Campus):
    uu = uuid.uuid1()
    db_campus = Campus(id=uu, name=campus.name, rank=campus.rank)
    db.add(db_campus)
    db.commit()
    db.refresh(db_campus)
    return db_campus