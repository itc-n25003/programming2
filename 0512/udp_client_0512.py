import socket

HOST = "127.0.0.1"
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"hello", (HOST, PORT))

data, address = client.recvfrom(4096)
print(data.decode("utf-8"))
print(address)

client.close()
