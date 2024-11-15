# tcp-python
Creación de un servidor TCP que interactúe con un cliente

## Instrucciones para ejecutar el servidor y el cliente

### Ejecutar el servidor
1. Abrir una terminal.
2. Navegar al directorio donde se encuentra el archivo `server.py`.
3. Ejecutar el siguiente comando:
   ```sh
   python server.py
4. El servidor inicia y escucha conexiones entrantes en 127.0.0.1:5000

### Ejecutar el cliente
1. Abrir otra terminal
2. Navegar al directorio donde se encuentra el archivo `client.py`.
3. Ejecutar el siguiente comando:
   ```sh
   python client.py
4. El cliente se conecta al servidor en 127.0.0.1:5000

### Realizar pruebas manuales
## Enviar un mensaje normal
1. En la terminal del cliente, ingresar un mensaje cualquiera y presionar la tecla Enter.
2. Verificar que el servidor reciba el mensaje y su respuesta sea el mismo en mayúsculas.
3. El cliente muestra la respuesta del servidor en mayúsculas

## Salir de la conexión
1. En la terminal del cliente, ingresar el mensaje "DESCONEXION" y presionar Enter.
2. Verificar que la conexión se cierra correctamente en ambos lados.
3. El servidor imprime un mensaje indicando que el cliente se ha desconectado.
4. De igual manera el cliente cierra la conexión y muestra un mensaje que la conexión se ha cerrado.

### Reconectar cliente
Si deseamos conectar otro cliente una vez que hemos cerrado una conexión previamente, podemos hacerlo nuevamente repitiendo los pasos al momento de ejecutar un cliente.