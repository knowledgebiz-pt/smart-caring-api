from websocket import create_connection, WebSocketApp
import json

 

ws = create_connection("ws://127.0.0.1:8000/private-chat", header=["id-user: 12345"])
ws.send(json.dumps({"user_id_sender": "12345", "user_id_receiver": "12345", "message": "Olá Oscar"}))
ws.close()