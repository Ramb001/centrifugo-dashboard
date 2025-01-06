import os

from src.centrifugo import CentrifugoApi
from src.pocketbase import Pocketbase

BOT_TOKEN = os.getenv("BOT_TOKEN")
POCKETBASE_URL = "http://127.0.0.1:8090"
CENTRIFUGO_API_KEY = os.getenv("CENTRIFUGO_API_KEY")
CENTRIFUGO_URL = "http://localhost:8000"
CENTRIFUGO_TOKEN_SECRET = os.getenv("CENTRIFUGO_TOKEN_SECRET")

CENTRIFUGO = CentrifugoApi(
    api_key=os.getenv("CENTRIFUGO_API_KEY"),
    base_url=CENTRIFUGO_URL,
    token_secret=os.getenv("CENTRIFUGO_TOKEN_SECRET"),
)
PB = Pocketbase(POCKETBASE_URL)


class PocketbaseCollections:
    USERS = "users"


class BotReplies:
    ON_BOARDING = "Hello! Centrifugo test bot started!"
