from websocket import create_connection, WebSocketApp
import json

 

ws = create_connection("ws://127.0.0.170:8000/private-chat", header=["id-user: 12345"])
ws.send(json.dumps({"user_id_sender": "12345", "user_id_receiver": "12345", "message": "Olá Oscar", "date": "04-03-2023", "deleted": False, "viewed": True, "sent": True, "id_user_sender": "12345", "id_user_receiver": "12345"}))
ws.close()