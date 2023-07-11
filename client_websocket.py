from websocket import create_connection, WebSocketApp
import json

ws = create_connection("ws://192.168.1.170:8000/private-chat", header=["id-user: 12345"])
print("Sending 'Hello, World'...")
ws.send(json.dumps({"id_user": "12345", "id_user_receiver": "1234", "message": "Olá Oscar"}))
print("Sent")
print("Receiving...")
result = ws.recv()
ws.send(json.dumps({"id_user": "12345", "id_user_receiver": "1234", "message": "Olá Oscar"}))
print("Received '%s'" % result)
ws.close()
