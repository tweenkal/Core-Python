import socket

s = socket.socket()
print("Socket is created")

s.bind(('localhost',5355))

s.listen(3)
print("Waiting for connections")

while True:
    c,address = s.accept()
    name = c.recv(1024).decode()
    print("Connection with=",address,name)
    c.send(bytes('welcome to teleusko','utf-8'))

    c.close()