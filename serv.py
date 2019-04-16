import socket
import os
import subprocess

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)

    while True:
        msg = con.recv(2048)
        if not msg: break
        print (cliente, msg.decode())
        msgd = msg.decode()

        if msgd[:3] == 'ls ':
            var = subprocess.getstatusoutput('ls')
            var1 = var[1]
            print(var1)
            con.send (var1.encode())

        elif msgd[:4] == 'get ':
            arqname = msgd[4:]
            arq = open(arqname, 'r')

            for i in arq.readlines():
                con.send(i.encode())
            arq.close()
    print ('Finalizando conexao do cliente', cliente)
    con.close()
