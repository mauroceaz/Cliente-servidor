import socket
import os
import subprocess

HOST = '127.0.0.1'
PORT = 5001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

def contentType(arq):
    ext = arq.split(".")
    if ext[-1] == "html":
        return "text/HTML"
    elif ext[-1] == "txt":
        return "text/txt"
    elif ext[-1] == "jpg":
        return "image/jpg"
    elif ext[-1] == "png":
        return "image/png"
    elif ext[-1] == "gif":
        return "image/gif"
    elif ext[-1] == "ico":
        return "image/ico"
    elif ext[-1] == "css":
        return "text/css"

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

        elif msgd[:5] == 'GET /':
            msgd = msgd[5:].split(" ")
            type = contentType(msgd[0])
            try:
                arq = open(msgd[0],'rb')
            except FileNotFoundError:
                print("404 Not Found")
            arq2 = arq.read()
            varl=len(arq2)
            header="HTTP/1.1 200 OK\r\n"
            header1="Content-Type: {}\r\n".format(type)
            header2="Content-Length: {}\r\n".format(varl)
            blank="\r\n"
            sendt=header.encode()+header1.encode()+header2.encode()+blank.encode()+arq2
            con.send(sendt)

        elif msgd[:7] == 'http://':
            url = msgd[7:]
            ca = (url , 5010)
            con.connect(ca)

    print ('Finalizando conexao do cliente', cliente)
    con.close()
