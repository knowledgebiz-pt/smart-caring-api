from websocket import create_connection, WebSocketApp
import json

ws = create_connection("ws://192.168.1.170:8000/private-chat", header=["id-user: 1234"])
print("Receiving...")
result = ws.recv()
ws.send(json.dumps({"id_user": "1234", "id_user_receiver": "12345", "message": "Olá João"}))
print("Received '%s'" % result)
ws.close()
