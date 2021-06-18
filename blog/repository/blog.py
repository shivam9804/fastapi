from sqlalchemy.orm import session
import schemas, models
from fastapi import status, HTTPException

def get_all(db: session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id, request, db: session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'successfully updated'

def destroy(id, db: session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail':'record deleted'}

def get(id, db: session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not avalilable")
    return blog