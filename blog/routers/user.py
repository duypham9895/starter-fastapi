from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from .. import schemas, database, models, hashing

router = APIRouter()

get_db = database.get_db
_hashing = hashing.Hash()


@router.post(
    "/user",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
    tags=["users"],
)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = _hashing.hash_password(request.password)
    new_user = models.User(
        name=request.name, email=request.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get(
    "/user/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
    tags=["users"],
)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {id}",
        )

    return user
