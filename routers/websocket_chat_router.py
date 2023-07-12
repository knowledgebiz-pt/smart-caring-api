import json
import base64
import os
import re
import time
from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import logging
from fastapi.logger import logger
import threading
import internal

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
logger.setLevel(gunicorn_logger.level)


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        print("SOMEONE CONNECTED")
        for item in websocket.headers.values():
            print(item)
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            logging.info("Total connections: " + str(len(self.active_connections)))
            print("Total connections: " + str(len(self.active_connections)))
            if connection.client_state.CONNECTED:
                await connection.send_text(message)

    async def send_message_to_user_id(self, message, id_user):
        user_receive = None
        for wb in self.active_connections:
            for hd in wb.headers.items():
                if hd[0] == "id-user":
                    if hd[1] == id_user:
                        user_receive = wb
        if user_receive is not None:
            await user_receive.send_text(message)


manager = ConnectionManager()


async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            body = json.loads(data)
            print(data)
            await manager.send_message_to_user_id(data, body["id_user_receiver"])
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client left the chat")
 