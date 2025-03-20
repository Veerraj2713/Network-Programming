import socket
s = socket.socket()

port = 56789

s.connect(('127.0.0.1', port))
print(s.recv(11024))
s.close()