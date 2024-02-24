from functools import lru_cache
from fastapi import Depends, FastAPI
from cassandra.cqlengine.management import sync_table
from contextlib import asynccontextmanager

from .users.models import User
from . import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Hello World")
    db.get_session()
    sync_table(User)
    yield
    print("Bbye World")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def get_session():
    return {"hello": "world"}


@app.get("/users")
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)
