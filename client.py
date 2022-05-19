import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 1024

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  
  msg = input("Ingrese un mensaje: ")
  msg_len = str(len(msg))
  msg_len += " " * (HEADER - len(msg_len))
  client.send(msg_len.encode("utf-8"))
  client.send(msg.encode("utf-8"))
