import socket

raj = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

raj.connect(("localhost", 2301))

message = raj.recv(2048)
print(f"Message Received : {message}")