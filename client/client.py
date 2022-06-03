import socket
import threading
import os

PORT = 56789
SERVER_IP = "192.168.1.84"
ADDR = (SERVER_IP, PORT)
NAME = os.getenv("USERNAME")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket, socket type and mode
client.connect(ADDR)
client.send(NAME.encode())

def send(msg):
    client.send(str(len(msg)).encode()) # send the lenght of the msg, on 255 bytes
    client.send(msg.encode()) # send the msg

def main():
    print(f"Successfully connected to {SERVER_IP}")
    print(f"Client IP : {socket.gethostbyname(socket.gethostname())}")
    print(f"Client name : {NAME}")
    print("=============================================================")
    while True:
        recv_msg = client.recv(255).decode()
        print(recv_msg)





thread = threading.Thread(target=main)
thread.start()

while True:
    msg = input()
    send(msg)