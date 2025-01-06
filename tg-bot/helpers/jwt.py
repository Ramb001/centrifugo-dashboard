import os
import jwt

SECRET_KEY = os.getenv("SECRET_KEY")


def generate_jwt_token(tg_id: int) -> str:
    payload = {
        "sub": str(tg_id),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
