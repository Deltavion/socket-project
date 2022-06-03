#------------------server------------------#
import socket
import threading

PORT = 56789
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)


def handle_client(client, addr):
    global clients_list
    global dns

    name = client.recv(255).decode()
    name = addr[1]  # localhost test
    dns[name] = addr[0]
    clients_list.append(client)

    print(f"[SERVER] new connection : {name}")
    print(f"[SERVER] clients connected : {len(clients_list)}")

    connected = True
    while connected:
        msg_lenght = client.recv(255).decode()
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = client.recv(msg_lenght).decode()

            # messages dont la réponse est envoyée uniquement au client qui à envoyer la requête
            if msg.startswith("-ip"):
                cmd = int(msg[4:msg_lenght])
                if cmd in dns:
                    resp = f"[SERVER] L'ip de {cmd} est {dns[cmd]}"

                else:
                    resp = f"[SERVER] Nom inconnu : l'utilisateur est inexistant ou déconnecté"

                client.send(resp.encode())
                print(resp)

            # messages dont la réponse est envoyée à tous les clients connectés
            else:
                if msg == "-quit":
                    connected = False
                    clients_list.remove(client)
                    msg = f'[SERVER] {name} disconnected'

                else:
                    msg = f'[{name}] {msg}'

                print(msg)
                for client_in_list in clients_list:
                    client_in_list.send(msg.encode())

    client.close()


def main():
    server.listen()
    print(f"[SERVER] listening on {SERVER_IP}:{PORT}")
    print("=============================================================")
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients_list = []
dns = {}

print("[SERVER] starting ...")
main()
