from .schemes import UserModel


__all__ = ("DATABASE", )


DATABASE = [
    UserModel(
        username="user",
        password="qwerty"
    )
]
