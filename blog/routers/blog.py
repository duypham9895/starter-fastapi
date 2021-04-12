from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder

from .. import schemas, database, models

router = APIRouter()

get_db = database.get_db


@router.get(
    "/blog",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ShowBlog],
    tags=["blogs"],
)
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get(
    "/blog/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
    tags=["blogs"],
)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )
    return blog


@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    blog.delete(synchronize_session=False)
    db.commit()
    return "DELETE done"


@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    blog.update(jsonable_encoder(request))
    db.commit()
    return "UPDATE done"
