from beanie import Document
from pydantic import EmailStr

from datetime import datetime, UTC


class User(Document):

    name: str
    email: EmailStr
    password: str

    created_at: datetime = datetime.now(UTC)