from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder

from .. import schemas, models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    blog.delete(synchronize_session=False)
    db.commit()

    return "DELETE done"


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    blog.update(jsonable_encoder(request))
    db.commit()
    return "UPDATE done"
