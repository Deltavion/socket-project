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

    def send(self, msg):
        print(msg)
        for client in self.clients_list:
            client.send(str(len(msg)).encode()) # send the lenght of the msg, on 255 bytes
            client.send(msg.encode()) # send the msg



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
                msg = client.recv(int(msg_lenght)).decode()
                msg = f"[{name}] {msg}"

                self.send(msg)

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
