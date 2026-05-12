from fastapi import APIRouter, Depends

from app.models.note_model import Note
from app.models.user_model import User

from app.utils.auth_utils import get_current_user

router = APIRouter()


@router.post("/notes")
async def create_note(
        title: str,
        content: str,
        current_user: User = Depends(get_current_user)
):

    new_note = Note(
        title=title,
        content=content,
        owner_email=current_user.email
    )

    await new_note.insert()

    return {
        "message": "Note created successfully"
    }


@router.get("/notes")
async def get_notes(
        current_user: User = Depends(get_current_user)
):

    notes = await Note.find(
        Note.owner_email == current_user.email
    ).to_list()

    return notes