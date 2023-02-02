import uuid
from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database.models.usersModel import User
from database.models.campusModel import Campus

from database.crud import campusCrud


# from auth import hashing_password

# from auth import hashing_password

# make a UUID based on the host address and current time
def gen_uuid():
    return uuid.uuid1()

def get_time():
    return datetime.now()

def get_user(db: Session, user_id: uuid.UUID):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    return user

def create_user(db: Session, user: User, campus: Campus):
    campus_id = campusCrud.get_campus(db, campus.name)
    if not campus_id:
        campusCrud.create_campus(db, campus)
    campus_id = campusCrud.get_campus(db, campus.name)
    uu = uuid.uuid1()
    db_user = User(id=uu, uname=user.uname, dname=user.dname, email=user.email, github="", rank=user.rank,
                      campus_id=campus_id.id, created_at=get_time())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


