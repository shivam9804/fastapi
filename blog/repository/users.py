from sqlalchemy.orm import session
import schemas, models
from hashing import Hash
from fastapi import status, HTTPException

def create(request:schemas.User, db:session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id, db:session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    
    return user