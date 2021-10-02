import os
import socket
resp=0

def inicio():
    #os.system('cls')
    print("|____Bienvenido__menu____|")
    print("|____1_Suma______________|")
    print("|____2_Resta_____________|")
    print("|____3_Multiplicacion____|")
    print("|____4_Division__________|")
    print("|____5_Modulo____________|")
    print("|____6_Potencia__________|")
    print("|____7_Cerrar____________|")

def leer_entrada():
   while True:
       try:
           resp = int(resp)
           return resp
       except ValueError:
           print ("La entrada es incorrecta: escribe un numero del 1 al 7")
           
while True:
    inicio()
    resp = input("|____Opción a realizar___|: ")

    print("\n")


    if resp == "1":
        print("|___________(+)_________ |")
        port = 9999
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect(("localhost",port))
        op = "1"
        ss.send(op.encode("ascii"))
        ip = ss.recv(1024).decode("ascii")
        pt = int(ss.recv(1024).decode("ascii"))
        ss.close()

        #SERVIDOR SUMA
        ss2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss2.connect((ip, pt))
    
        v1 = input("|          Num 1         | ")
        v2 = input("|          Num 2         | ")

        ss2.send(v1.encode("ascii"))
        ss2.send(v2.encode("ascii"))
        resultado = ss2.recv(1024)
        ss2.close()

        print("|          Total         | {} + {} = {}".format(v1, v2, resultado.decode("ascii")))
        print("\n")


    elif resp == "2" :
        print("|___________(-)_________ |")
        port = 9999
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect(("localhost",port))
        op = "2"
        ss.send(op.encode("ascii"))
        ip = ss.recv(1024).decode("ascii")
        pt = int(ss.recv(1024).decode("ascii"))
        ss.close()

        #SERVIDOR RESTA
        ss2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss2.connect((ip, pt))

        v1 = input("|          Num 1         | ")
        v2 = input("|          Num 2         | ")

        ss2.send(v1.encode("ascii"))
        ss2.send(v2.encode("ascii"))
        resultado = ss2.recv(1024)
        ss2.close()

        print("|          Total         | {} - {} = {}".format(v1, v2, resultado.decode("ascii")))
        print("\n")

    elif resp == "3":
        print("|___________(*)_________ |")
        port = 9999
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect(("localhost",port))
        op = "3"
        ss.send(op.encode("ascii"))
        ip = ss.recv(1024).decode("ascii")
        pt = int(ss.recv(1024).decode("ascii"))
        ss.close()

        ##SERVIDOR MULT
        ss2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss2.connect((ip, pt))

        v1 = input("|          Num 1         | ")
        v2 = input("|          Num 2         | ")

        ss2.send(v1.encode("ascii"))
        ss2.send(v2.encode("ascii"))
        resultado = ss2.recv(1024)
        ss2.close()

        print("|          Total         | {} * {} = {}".format(v1, v2, resultado.decode("ascii")))
        print("\n")
        
    elif resp == "4":
        print("|___________(/)_________ |")
        port = 9999
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect(("localhost",port))
        op = "4"
        ss.send(op.encode("ascii"))
        ip = ss.recv(1024).decode("ascii")
        pt = int(ss.recv(1024).decode("ascii"))
        ss.close()

        #SERVIDOR DIV
        ss2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss2.connect((ip, pt))

        v1 = input("|          Num 1         | ")
        v2 = input("|          Num 2         | ")

        ss2.send(v1.encode("ascii"))
        ss2.send(v2.encode("ascii"))
        resultado = ss2.recv(1024)
        ss2.close()

        print("|          Total         | {} / {} = {}".format(v1, v2, resultado.decode("ascii")))
        print("\n")
        
    elif resp == "5":
        print("|___________(%)_________ |")
        port = 9999
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect(("localhost",port))
        op = "5"
        ss.send(op.encode("ascii"))
        ip= ss.recv(1024).decode("ascii")
        pt = int(ss.recv(1024).decode("ascii"))
        ss.close()

        #SERVIDOR MOD
        ss2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss2.connect((ip, pt))

        v1 = input("|          Num 1         | ")
        v2 = input("|          Num 2         | ")

        ss2.send(v1.encode("ascii"))
        ss2.send(v2.encode("ascii"))
        resultado = ss2.recv(1024)
        ss2.close()

        print("|          Total         | {} % {} = {}".format(v1, v2, resultado.decode("ascii")))
        print("\n")
        
    elif resp == "6":
        print("|___________(^)_________ |")
        port = 9999
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect(("localhost",port))
        op = "6"
        ss.send(op.encode("ascii"))
        ip = ss.recv(1024).decode("ascii")
        pt = int(ss.recv(1024).decode("ascii"))
        ss.close()

        #SERVIDOR POT
        ss2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss2.connect((ip,pt))

        v1 = input("|          Num 1         | ")
        v2 = input("|          Num 2         | ")

        ss2.send(v1.encode("ascii"))
        ss2.send(v2.encode("ascii"))
        resultado = ss2.recv(1024)
        ss2.close()

        print("|          Total         | {} ^ {} = {}".format(v1, v2, resultado.decode("ascii")))
        print("\n")

    else:
        print ("¿Por qué no intentas elegir una opción entre [1-7]? ")
        print("\n")

        
