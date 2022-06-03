import socket
import threading

class Server:
    def __init__(self, adress):
        self.clients_list = []
        self.dns = {}

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(adress)
        self.server_socket.listen()

    def listen_to_client(self):
        client, addr = self.server_socket.accept()
        thread = threading.Thread(target=self.handle_client, args=(client, addr))
        thread.start()

    def global_msg(self, msg):
        print(msg)
        for client in self.clients_list:
            client.send(msg.encode())



    def handle_client(self, client, addr):
        name = client.recv(255).decode()
        name = addr[1]  # localhost test
        self.dns[name] = addr[0]
        self.clients_list.append(client)

        self.global_msg(f"[SERVER] New connection : {name}")

        connected = True
        while connected:
            msg_lenght = client.recv(255).decode()
            if msg_lenght:
                msg_lenght = int(msg_lenght)
                msg = client.recv(msg_lenght).decode()

                msg = f'[{name}] {msg}'

                self.global_msg(msg)

        client.close()

PORT = 56789
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)


print("[SERVER] Starting ...")
server = Server(ADDR)
print(f"[SERVER] Listening on {SERVER_IP}:{PORT}")
print("=============================================================")

running = True
while running:
    server.listen_to_client()
