import socket
import threading
import os
import ast
import gui
import time

#=====================================================================constants
PORT = 56789
SERVER_IP = "192.168.1.84"
SERVER_ADDR = (SERVER_IP, PORT)
NAME = os.getenv("USERNAME")
# create a socket, socket type and mode
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#=====================================================================functions
def backend():
    global app
    print("backend")
    time.sleep(3)
    app.refresh_client()
    print("back")

    # # connection
    # CLIENT_SOCKET.connect(SERVER_ADDR)
    # # sending name
    # CLIENT_SOCKET.send(NAME.encode())
    # # receiving dns
    # dns_str_lenght = CLIENT_SOCKET.recv(255).decode()
    # if dns_str_lenght:
    #     dns_str = CLIENT_SOCKET.recv(int(dns_str_lenght)).decode()
    #     dns = ast.literal_eval(dns_str)


    # print(f"Successfully connected to {SERVER_IP}")
    # print(f"Client IP : {socket.gethostbyname(socket.gethostname())}")
    # print(f"Client name : {NAME}")
    # print("=============================================================")

    # print(f"LOG {dns}") #test

    # running = True
    # while running:
    #     handle_message()



def send(msg, socket):
    # send the lenght of the msg, on 255 bytes
    socket.send(str(len(msg)).encode())
    socket.send(msg.encode())  # send the msg


def handle_input():
    msg = input()
    if msg:
        send(msg, CLIENT_SOCKET)
    if msg == "!quit":
        pass

def handle_message():
    msg_lenght = CLIENT_SOCKET.recv(255).decode()
    if msg_lenght:
        msg = CLIENT_SOCKET.recv(int(msg_lenght)).decode()
        print(msg)

#=====================================================================variables


#==========================================================================main
app = gui.SocketApp()
threading.Thread(target=backend).start()
app.run()
