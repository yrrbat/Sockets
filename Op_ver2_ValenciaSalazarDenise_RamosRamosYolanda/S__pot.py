import socket
#import time
port = 6000
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(("localhost", port))
ss.listen(10)

while True:
    cs, addr = ss.accept()
    print ("Servidor potencia conectado correctamente", addr)  
    v1 = float(cs.recv(1024).decode("ascii"))
    v2 = float(cs.recv(1024).decode("ascii"))
    cs.send(str (v1 ** v2).encode("ascii"))
    cs.close()
