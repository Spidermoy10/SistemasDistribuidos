import socket

def send_audio(client_socket):
    with open('test.wav', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)

    print("Servidor escuchando en el puerto 9999...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Conexión establecida desde {address}")
        send_audio(client_socket)
        client_socket.close()

if __name__ == "__main__":
    main()
