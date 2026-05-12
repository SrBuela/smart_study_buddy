from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.db import connect_db
from app.routes.auth_routes import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    await connect_db()

    yield


app = FastAPI(
    lifespan=lifespan
)


app.include_router(auth_router)


@app.get("/")
async def home():

    return {
        "message": "Smart Study Buddy API Running"
    }