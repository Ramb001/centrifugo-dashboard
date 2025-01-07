import os
from cent import Client

CENTRIFUGO_API_KEY = os.getenv("CENTRIFUGO_API_KEY")
CENTRIFUGO_URL = "http://localhost:8000/api"
CENTRIFUGO_CLIENT = Client(CENTRIFUGO_URL, api_key=CENTRIFUGO_API_KEY)

SECRET_KEY = os.getenv("SECRET_KEY")
