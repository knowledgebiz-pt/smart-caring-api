from websocket import create_connection, WebSocketApp
import json

 

ws = create_connection("ws://192.168.1.170:8000/private-chat", header=["id-user: 12345"])
ws.send(json.dumps({"user_id_sender": "12345", "id_user_receiver": "12345", "message": "Olá Oscar"}))
ws.close()