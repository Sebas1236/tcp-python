import socket 

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024 # Tamaño del buffer para recibir datos

# Creamos un socket, para el protocolo TCP utilizamos:
# AF_INET: IPv4, SOCK_STREAM: TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos al servidor
client_socket.connect((HOST, PORT))
print(f"Conectado a {HOST}:{PORT}")

try:
    while True:
        # Enviamos un mensaje al servidor
        message = input("Ingrese un mensaje (o ingresa 'DESCONEXION' para salir): ").strip()
        client_socket.sendall(message.encode())
        # Si el mensaje es 'DESCONEXION' cerramos la conexión
        if message.upper() == 'DESCONEXION':
            break
        # Recibimos la respuesta del servidor
        data = client_socket.recv(BUFFER_SIZE)
        print(f"Respuesta del servidor: {data.decode()}")
# Validamos cualquier excepción
except Exception as e:
    print(f"Error de conexión: {e}")
# Nos aseguramos de cerrar la conexión
finally:
    client_socket.close()
    print("Conexión cerrada")