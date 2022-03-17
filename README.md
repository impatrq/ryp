# Socket TCP

## Consigna

1- Crear un `server.py` y `socket.py`

2- Establecer una conexion servidor-cliente donde:

  - El cliente pueda mandar cualquier mensaje desde la consola a partir de un mensaje como `Ingrese un mensaje: `
  - El servidor le conteste `Recibido`
  - La conexion debe durar hasta que el cliente envie `close`

Deberia verse algo parecido a esto:

`server.py`

```
[LISTENING] El servidor esta esperando conexiones en 192.168.56.1
[CONNECTED] Nueva conexion en ('192.168.56.1', 59616)
[CLIENT] Hola, que tal?
[CLIENT] Todo bien?

```

`client.py`

```
[CONNECTED] Conectado al servidor en 192.168.56.1
[CLIENT] Ingrese un mensaje: Hola, como estas?
[SERVER] Recibido!
[CLIENT] Ingrese un mensaje: Todo bien?
[SERVER] Recibido!
[CLIENT] Ingrese un mensaje: 
```

3- Hacer un `README.md` con el siguiente contenido:

```markdown
# Socket TCP


Alumno: Nombre y apellido

Curso: Curso

Materia: Redes y Protocolos

```

## Orientacion

- Documentacion de [socket](https://docs.python.org/3/library/socket.html)

## Entrega

- Crear un repositorio con el nombre `ryp-01`
- Subir el `README.md`, `server.py` y `client.py`
