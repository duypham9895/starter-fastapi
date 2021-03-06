from fastapi import FastAPI
from fastapi import status

from blog import models
from blog.routers import blog, user, authentication

from blog.database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get(
    "/",
    status_code=status.HTTP_200_OK,
)
def hello():
    return {"detail": "ok"}


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
