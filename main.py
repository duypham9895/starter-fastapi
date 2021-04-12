from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

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


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": {"title": "Create a Blog", "content": blog}}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9000)
