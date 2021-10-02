import socket
port = 9999
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(("", port))
ss.listen(10)
sv = []

"""
def final():
    global sv
    #lista
4    print(sv)
    return
"""
while True:
    cs, addr = ss.accept()
    print ("Conectado al servidor oficial", addr)
    sv.append(addr)
    op = int(cs.recv(1024).decode("ascii"))

##REALIZAR LA COMUNICACIÓN DEL USUARIO Y SERVIDOR DE LA OP

    #|||||||---SUMA PUERTO 5050
    if(op == 1):
        cs.send("localhost".encode("ascii"))
        cs.send("5050".encode("ascii"))
        cs.close()
    #|||||||---RESTA PUERTO 5060
    elif(op == 2):
        cs.send("localhost".encode("ascii"))
        cs.send("5060".encode("ascii"))
        cs.close()
    #|||||||---MUL PUERTO 5070
    elif(op == 3):
        cs.send("localhost".encode("ascii"))
        cs.send("5070".encode("ascii"))
        cs.close()
    #|||||||---DIV PUERTO 5080
    elif(op == 4):
        cs.send("localhost".encode("ascii"))
        cs.send("5080".encode("ascii"))
        cs.close()
    #|||||||---MOD PUERTO 5090
    elif(op == 5):
        cs.send("localhost".encode("ascii"))
        cs.send("5090".encode("ascii"))
        cs.close()
    #|||||||---POT PUERTO 6000 
    elif(op == 6):
        cs.send("localhost".encode("ascii"))
        cs.send("6000".encode("ascii"))
        cs.close()
             


             
