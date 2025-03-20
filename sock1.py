import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname('www.github.com')
print(ip)