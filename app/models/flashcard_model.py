from beanie import Document
from pydantic import Field
from datetime import datetime, UTC


class Flashcard(Document):

    question: str
    answer: str

    owner_email: str

    ease_factor: float = 2.5

    interval: int = 1

    repetitions: int = 0

    next_review: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    class Settings:
        name = "flashcards"