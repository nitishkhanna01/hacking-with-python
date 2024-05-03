import socket
domain= input("Enter Domain you want to know ip of : ")
print("Ip of "+domain+" : "+socket.gethostbyname(domain))
