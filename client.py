import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 0

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  pass
