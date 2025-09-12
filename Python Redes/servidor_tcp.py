import socket

class ServidorTCP():
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor TCP escuchando en {self.host}:{self.port}")

    def iniciar(self):
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"Conexão estabecida com {addr}")
                self.handle_client(client_socket)
        except KeyboardInterrupt:
            print("\nServidor encerrado.")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket):
        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Recebido: {data.decode()}")
                client_socket.sendall(data)
                print(f"Enviado: {data.decode()}")  


if __name__ == "__main__":
    servidor = ServidorTCP()
    servidor.iniciar()

