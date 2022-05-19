import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 1024

server = socket.socket()
server.bind((IP, PORT))
server.listen()
print(f"[LISTENING] El servidor esta esperando conexiones en {IP}")

conn, addr = server.accept()
print(f"[CONNECTED] Nueva conexion en {addr}")

while True:
  
  msg_len = int(conn.recv(HEADER).decode("utf-8"))
  msg = conn.recv(msg_len).decode("utf-8")
  print(f"[CLIENT] El cliente dice: {msg}")
