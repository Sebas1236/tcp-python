import socket

# Servidor iniciado en localhost
HOST = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 1024 # Tamaño del buffer para recibir datos

# Creamos un socket, para el protocolo TCP utilizamos:
# AF_INET: IPv4, SOCK_STREAM: TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket al host y puerto
server_socket.bind((HOST, PORT))

# Escuchamos conexiones entrantes
server_socket.listen()
print(f"Servidor iniciado en {HOST}:{PORT}")

while True:
    # Aceptamos conexiones entrantes
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante de {client_address}")

    # Manejamos múltiples mensajes del cliente
    try:
        while True:
            # Recibimos datos del cliente
            data = client_socket.recv(BUFFER_SIZE)
            # Si el cliente se desconecta o envía el mensaje 'DESCONEXION'
            if not data or data.decode('utf-8').upper() == 'DESCONEXION':
                print(f"Cliente desconectado {client_address}")
                break
            print(f"Mensaje recibido: {data.decode()}")

            # Responder al cliente devolviendo el mensaje en mayúsculas
            client_socket.sendall(data.upper())
    # Validamos cualquier excepción
    except Exception as e:
        print(f"Error de conexión: {e}")
    # Nos aseguramos de cerrar la conexión
    finally:
        client_socket.close()
        print(f"Conexión cerrada con {client_address}")
