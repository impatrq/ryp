import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 0

server = socket.socket()
server.bind((IP, PORT))
server.listen()
print(f"[LISTENING] El servidor esta esperando conexiones en {IP}")

while True:
  pass
