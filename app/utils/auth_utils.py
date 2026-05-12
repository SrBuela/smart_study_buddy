from jose import jwt
from datetime import datetime, timedelta, UTC

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.models.user_model import User

SECRET_KEY = "mysupersecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


async def get_current_user(
        token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = await User.find_one(
            User.email == email
        )

        if user is None:

            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )