import jwt
from fastapi import APIRouter, HTTPException

from cent import PublishRequest

from src.constants import CENTRIFUGO_CLIENT, SECRET_KEY
from src.storage import sid_list, sid_storage, SidData

router = APIRouter()


@router.get("/token/auth")
async def generate_jwt_auth_token(user_id: str):
    payload = {
        "sub": user_id,
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token


@router.get("/token/channel")
async def generate_jwt_channel_token(user_id: str, channel: str):
    payload = {"sub": user_id, "channel": channel}

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token


@router.post("/sid/save")
async def save_sid(data: SidData):
    sid_storage[data.user_id] = data.sid

    if data.sid not in sid_list:
        sid_list.append(data.sid)

    return {
        "message": "SID saved successfully and subscribed to channel",
        "current_sids": sid_list,
    }


@router.post("/message/send")
async def send_message():
    message = {"text": "Новое уведомление для вас!!!"}
    try:
        CENTRIFUGO_CLIENT._send(PublishRequest(channel="general", data=message))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {e}")

    return {"message": "Notification sent successfully"}
