import socket
s = socket.socket()
print('socket successfully created')

port = 56789

s.bind(("", port))

print(f'socket binded to port {port}')
s.listen(5)
print('socket is listening')
while True :
    c,addr = s.accept()
    print('Got conection from', addr)
    message = ('Thankyou for connecting')
    c.send(message.encode())
    c.close()