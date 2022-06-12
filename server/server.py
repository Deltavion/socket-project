import socket
import threading

#=====================================================================functions
def handle_client(client_socket, addr):
    clients_socket.append(client_socket)

    name = client_socket.recv(255).decode()
    name = addr[1]  # TEST, REMOVE TO PROD
    dns[name] = addr[0]
    dns_str = str(dns)
    client_socket.send(str(len(dns_str)).encode())
    client_socket.send(dns_str.encode())

    send(f"[SERVER] New connection : {name}", client_socket)

    connected = True
    while connected:
        msg_lenght = client_socket.recv(255).decode()
        if msg_lenght:
            msg = client_socket.recv(int(msg_lenght)).decode()
            if msg == "!quit":
                connected = False
            else:
                msg = f"[{name}] {msg}"
                send(msg, client_socket)

    client_socket.close()
    clients_socket.remove(client_socket)
    dns.pop(name)
    send(f"[SERVER] Deconnection : {name}", client_socket)


def send(msg, exp_socket):
    print(msg)
    for client_socket in clients_socket:
        if exp_socket != client_socket:
            client_socket.send(str(len(msg)).encode())# send the lenght of the msg, on 255 bytes
            client_socket.send(msg.encode())  # send the msg

#=====================================================================constants
PORT = 56789
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#=====================================================================variables
clients_socket = []
clients = []
dns = {}

#==========================================================================main
print("[SERVER] Starting ...")
SERVER_SOCKET.bind(ADDR)
SERVER_SOCKET.listen()
print(f"[SERVER] Listening on {SERVER_IP}:{PORT}")
print("=============================================================")

running = True
while running:
    client, addr = SERVER_SOCKET.accept()
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.start()