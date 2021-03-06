from fastapi import FastAPI

from . import models
from .routers import blog, user, authentication

from blog.database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
