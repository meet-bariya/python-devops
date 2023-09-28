from src import wiki
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API Endpoints: /search /wiki"}


@app.get("/search/{name}")
async def search(name):
    result = wiki.search(name)
    return {"result": result}


@app.get("/wiki/{name}")
async def summary(name):
    result = wiki.summary(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
