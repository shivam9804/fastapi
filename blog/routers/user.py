from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session
from repository import users

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return users.create(request, db)
    # return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def user(id, db: Session = Depends(get_db)):
    # return user.show_user(id, db)
    return users.show(id, db)