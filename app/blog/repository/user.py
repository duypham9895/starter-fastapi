from sqlalchemy.orm import Session
from fastapi import status, HTTPException

from blog import schemas, models, hashing

_hashing = hashing.Hash()


def create(request: schemas.User, db: Session):
    hashed_password = _hashing.hash_password(request.password)
    new_user = models.User(
        name=request.name, email=request.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    return user
