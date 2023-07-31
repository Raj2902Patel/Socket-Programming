import socket

raj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


raj.bind(("localhost", 2301))
raj.listen(5)

while True:
    clientSocket, address = raj.accept()
    print(f"Connection Establishedd From Address {address}")
    clientSocket.send(bytes("Welcome to the server!" , "utf-8"))
    clientSocket.close()