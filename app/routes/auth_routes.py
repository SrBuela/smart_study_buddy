from fastapi import APIRouter, Depends

from app.models.user_model import User

from app.utils.hashing import (
    hash_password,
    verify_password
)

from app.utils.auth_utils import (
    create_access_token,
    get_current_user
)

router = APIRouter()


@router.post("/signup")
async def signup(
        name: str,
        email: str,
        password: str
):

    existing_user = await User.find_one(
        User.email == email
    )

    if existing_user:

        return {
            "message": "User already exists"
        }

    hashed_pw = hash_password(password)

    new_user = User(
        name=name,
        email=email,
        password=hashed_pw
    )

    await new_user.insert()

    return {
        "message": "User created successfully"
    }


@router.post("/login")
async def login(
        email: str,
        password: str
):

    user = await User.find_one(
        User.email == email
    )

    if not user:

        return {
            "message": "User not found"
        }

    password_correct = verify_password(
        password,
        user.password
    )

    if not password_correct:

        return {
            "message": "Incorrect password"
        }

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "message": "Login successful",
        "access_token": access_token
    }


@router.get("/me")
async def get_me(
        current_user: User = Depends(get_current_user)
):

    return {
        "name": current_user.name,
        "email": current_user.email
    }