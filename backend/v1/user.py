from typing import List

from jose import jwt, JWTError
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

import auth

# from main import get_current_user

from database.models.usersModel import User
from database.crud import userCrud
from database.db import SessionLocal
from database.schemas import usersSchema, campusSchema

router = APIRouter(
    prefix='/user'
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/{user_id}')
def get_user_by_id(id: str, db: Session = Depends(get_db)):
    return userCrud.get_user(db, id)

@router.post('')
def create_user(current_user: usersSchema.UserRequest, campus: campusSchema.CampusRequest, db: Session = Depends(get_db)):
    return userCrud.create_user(db, current_user, campus)

