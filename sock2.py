import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket successfully created!")
except socket.error as err:
    print(f"socket creaation failed with error {err}")

port = 80

try:
    host_ip = socket.gethostbyname("www.github.com")
except socket.gaierror:
    print('error resolving the host')
    sys.exit()

s.connect((host_ip, port))
print(f'socket has successfully connected to Github on port == {host_ip}')