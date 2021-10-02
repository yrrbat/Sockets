import socket
port = 5070
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(("localhost", port))
ss.listen(10)

while True:
    cs, addr = ss.accept()
    print ("Servidor multiplicación conectado correctamente", addr)  
    v1 = int(cs.recv(1024).decode("ascii"))
    v2 = int(cs.recv(1024).decode("ascii"))
    cs.send(str(v1 *v2).encode("ascii"))
    cs.close()
