import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5001            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input().encode()
#arq = open('file','w')
while msg != '\x18':
    tcp.send (msg)
    var1 = tcp.recv(4096)
    print (var1.decode())
    msg = input().encode()
    #arq.write(var1.decode())

tcp.close()
