from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv
import os

from app.models.user_model import User

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URL)

database = client[DATABASE_NAME]


async def connect_db():
    await init_beanie(
        database=database,
        document_models=[User]
    )

    print("✅ MongoDB Connected Successfully")