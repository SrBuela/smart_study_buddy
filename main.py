from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.db import connect_db

from app.routes.auth_routes import router as auth_router
from app.routes.note_routes import router as note_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    await connect_db()

    print("✅ MongoDB Connected Successfully")

    yield

    print("🔴 Server shutting down")


app = FastAPI(
    title="Smart Study Buddy",
    lifespan=lifespan
)

# Routers
app.include_router(auth_router)
app.include_router(note_router)


@app.get("/")
def root():

    return {
        "message": "Smart Study Buddy running 🚀"
    }