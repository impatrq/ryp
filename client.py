import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 0

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  
  client.send(input("Ingrese un mensaje: ").encode("utf-8"))
  msg = client.recv(1024).decode("utf-8")
  print(f"[SERVER] Servidor dice: {msg}")

