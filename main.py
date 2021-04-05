from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "duy"}}


@app.get("/about")
def about():
    return {"data": {"name": "about page"}}
