import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('locallhost.com', 80)
client_socket.connect(server_address)

request_header = 'GET / HTTP/1.1\r\nHost: locallhost.com/\r\nConnection: keep-alive\r\n\ Content-Length: 0\r\n\r\n'
client_socket.send(request_header.encode())

while True:
    recv = client_socket.recv(1024)
    print (recv.decode())
    if not recv:
        break

client_socket.close()
