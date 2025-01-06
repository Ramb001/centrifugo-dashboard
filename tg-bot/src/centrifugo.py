import time
import aiohttp
import asyncio
import json
import websockets


class CentrifugoApi:
    def __init__(self, api_key: str, base_url: str, token_secret: str):
        self.__api_key = api_key
        self.__base_url = base_url
        self.__token_secret = token_secret
        self.__ws_url = f"{self.__base_url}/connection/http_stream"

    async def __get_headers(self, client: aiohttp.ClientSession):
        return {
            "Authorization": f"apikey {self.__api_key}",
            "X-Centrifugo-Token": self.__token_secret,
        }

    async def connect_to_websocket(self):
        try:
            async with websockets.connect(self.__ws_url) as websocket:
                auth_message = {
                    "method": "authenticate",
                    "params": {"token": self.__token},
                }
                await websocket.send(json.dumps(auth_message))

                while True:
                    response = await websocket.recv()
                    print(f"Received: {response}")
        except Exception as e:
            print(f"Error connecting to WebSocket: {e}")


    async def subscribe(
        self, client: aiohttp.ClientSession, channel: str, user_id: str, data: dict
    ):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={
                "method": "subscribe",
                "params": {"channel": channel, "user_id": user_id},
            },
            headers=headers,
        ) as resp:
            response = await resp.json()
            if "error" in response:
                print(f"Failed to subscribe: {response['error']}")
            else:
                print(f"Successfully subscribed to channel: {channel}")
            return response

    async def publish_message(
        self, channel: str, data: dict, client: aiohttp.ClientSession
    ):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "publish", "params": {"channel": channel, "data": data}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def fetch_presence(self, channel: str, client: aiohttp.ClientSession):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "presence", "params": {"channel": channel}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def fetch_channels(self, client: aiohttp.ClientSession):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "channels", "params": {}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def get_info(self, client: aiohttp.ClientSession):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "info", "params": {}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def send_push_notification(
        self, channel: str, title: str, body: str, client: aiohttp.ClientSession
    ):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={
                "method": "push",
                "params": {
                    "channel": channel,
                    "notification": {"title": title, "body": body},
                },
            },
            headers=headers,
        ) as resp:
            return await resp.json()

    async def unsubscribe(
        self, client: aiohttp.ClientSession, channel: str, user_id: str
    ):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={
                "method": "unsubscribe",
                "params": {"channel": channel, "user_id": user_id},
            },
            headers=headers,
        ) as resp:
            return await resp.json()

    async def get_history(
        self, channel: str, limit: int, client: aiohttp.ClientSession
    ):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "history", "params": {"channel": channel, "limit": limit}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def send_message_to_user(
        self, channel: str, user_id: str, data: dict, client: aiohttp.ClientSession
    ):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={
                "method": "publish",
                "params": {"channel": f"{channel}:{user_id}", "data": data},
            },
            headers=headers,
        ) as resp:
            return await resp.json()

    async def get_connections(self, client: aiohttp.ClientSession):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "connections", "params": {}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def get_presence_stats(self, client: aiohttp.ClientSession):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "presence_stats", "params": {}},
            headers=headers,
        ) as resp:
            return await resp.json()

    async def get_subscriptions(self, client: aiohttp.ClientSession):
        headers = await self.__get_headers(client)
        async with client.post(
            f"{self.__base_url}/api",
            json={"method": "subscriptions", "params": {}},
            headers=headers,
        ) as resp:
            return await resp.json()
