from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    return {
        "data": {
            "title": "blog list",
            "limit": limit,
            "published": published,
            "sort": sort,
        }
    }


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": {"id": id}}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10, sort: Optional[str] = None):
    return {
        "data": {
            "id": id,
            "comments": ["hii", "great!!", "555"],
            "limit": limit,
            "sort": sort,
        }
    }
