import socket
import threading
import os
import ast

#=====================================================================functions
def send(msg, socket):
    # send the lenght of the msg, on 255 bytes
    socket.send(str(len(msg)).encode())
    socket.send(msg.encode())  # send the msg


def handle_input():
    global running
    while running:
        msg = input()
        if msg:
            send(msg, CLIENT_SOCKET)
        if msg == "!quit":
            running = False
#=====================================================================constants
PORT = 56789
SERVER_IP = "192.168.1.84"
SERVER_ADDR = (SERVER_IP, PORT)
NAME = os.getenv("USERNAME")
# create a socket, socket type and mode
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#=====================================================================variables
running = True

#==========================================================================main
# connection
CLIENT_SOCKET.connect(SERVER_ADDR)
# sending name
CLIENT_SOCKET.send(NAME.encode())
# receiving dns
dns_str_lenght = CLIENT_SOCKET.recv(255).decode()
if dns_str_lenght:
    dns_str = CLIENT_SOCKET.recv(int(dns_str_lenght)).decode()
    dns = ast.literal_eval(dns_str)


print(f"Successfully connected to {SERVER_IP}")
print(f"Client IP : {socket.gethostbyname(socket.gethostname())}")
print(f"Client name : {NAME}")
print("=============================================================")
#CLIENT_SOCKET.recv(255)

thread = threading.Thread(target=handle_input)
thread.start()
print(f"LOG {dns}")
while running:
    msg_lenght = CLIENT_SOCKET.recv(255).decode()
    if msg_lenght:
        msg = CLIENT_SOCKET.recv(int(msg_lenght)).decode()
        print(msg)

