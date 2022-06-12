import socket
import ast

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.84", 56789))
print("connected to server")

dns_str_lenght = client.recv(255).decode()
if dns_str_lenght:
    dns_str = client.recv(int(dns_str_lenght)).decode()
    dns = ast.literal_eval(dns_str)

print(dns)