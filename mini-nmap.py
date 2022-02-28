# Simple Scan ports
import socket

print("Url: ")
letsgo = input()

ports = [21,22,23,443,80,8080]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    codigo = client.connect_ex((letsgo, port))
    
    if codigo == 0:
        print (port, "OPEN")
