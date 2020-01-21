import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncConsumer):
    def websocket_connect(self, event):
        print("connected: ", event)

    def websocket_receive(self, event):
        print("Received : ", event)

    def websocket_disconnect(self, event):
        print("Disconnected: ", event)
