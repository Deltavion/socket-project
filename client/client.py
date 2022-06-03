#------------------client------------------#
import socket
import threading
from tkinter import *
import os

PORT = 56789
SERVER_IP = "192.168.1.84"
ADDR = (SERVER_IP, PORT)
NAME = os.getenv("USERNAME")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket, socket type and mode
client.connect(ADDR)
name_encoded = NAME.encode()
client.send(name_encoded)

def send(msg):
    msg = msg.encode()
    lenght = str(len(msg)).encode()

    client.send(lenght)
    client.send(msg)

def main():
    global run
    print(f"Successfully connected to {SERVER_IP}")
    print(f"Client IP : {socket.gethostbyname(socket.gethostname())}")
    print(f"Client name : {NAME}")
    print("=============================================================")
    while run:
        recv_msg = client.recv(255).decode()
        print(recv_msg)

def clicked():
    global run
    global text_input
    msg = text_input.get()
    text_input.delete(0,END)
    if msg:
        if msg == "-quit":
            app.destroy()
            run = False
        send(msg)

app = Tk()

text_input = Entry(app, width=50)
text_input.pack(padx=5, pady=5, side=LEFT)
text_input.focus_force()

btnAffiche = Button(app, text='Send', command=clicked)
btnAffiche.pack(padx=5, pady=5)

run = True
thread = threading.Thread(target=main)
thread.start()
app.mainloop()