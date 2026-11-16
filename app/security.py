import secrets
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from .schemes import UserModel
from .database import DATABASE


__all__ = ("auth_user", )

security = HTTPBasic()


def auth_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]) -> UserModel:

    unauth_user_exp = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Пользователь не авторизован",
        headers={
            "WWW-Authenticate": "Basic"
        }
    )

    for user in DATABASE:
        # Защита от атаки по временем
        username_compare_digest = secrets.compare_digest(user.username.encode("utf-8"), credentials.username.encode("utf-8"))
        password_compare_digest = secrets.compare_digest(user.password.encode("utf-8"), credentials.password.encode("utf-8"))

        if username_compare_digest and password_compare_digest:
            return user

    raise unauth_user_exp
