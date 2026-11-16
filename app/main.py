from fastapi import FastAPI, Depends
from .security import auth_user
from .schemes import UserModel

app = FastAPI()


@app.get("/login")
def login_endpoint(user: UserModel = Depends(auth_user)) -> dict[str, str]:
    return {
        "message": "You got my secret, welcome"
    }
