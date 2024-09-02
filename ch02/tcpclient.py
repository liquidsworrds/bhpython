import socket

target_host = "0.0.0.0"
target_port = 1337

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to client
client.connect((target_host, target_port))

client.send(b"ABCDEF")

response = client.recv(4096)

print(response.decode())
client.close()
