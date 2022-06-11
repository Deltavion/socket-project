import socket

dns = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.84", 56789))
server.listen()
print("listening")
client, addr = server.accept()
dns[addr[0]] = addr[1]
print("client connected")
print("=======================")

dns_str = str(dns)
client.send(str(len(dns_str)).encode())
client.send(dns_str.encode())
