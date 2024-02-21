from functools import lru_cache
from astrapy.db import AstraDB
from fastapi import Depends, FastAPI

from .config import Settings


@lru_cache
def get_settings():
    return Settings()


app = FastAPI()


@app.get("/")
def get_session(settings: Settings = Depends(get_settings)):
    db = AstraDB(
        token=settings.DB_TOKEN,
        api_endpoint=settings.DB_ENDPOINT)
    print(f"Connected to Astra DB: {db.get_collections()}")
    return {"hello": "world"}


@app.get("/")
async def hello_world():
    return {"hello": "world"}
