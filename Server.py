'''
referencias:
    https://www.youtube.com/watch?v=Lbfe3-v7yE0
    https://youtu.be/WM1z8soch0Q

'''

from Emisor import *
import socket


HEADERSIZE = 10



# se define el objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

# conexiones 
while True:
    c_socket, ip_addr = s.accept()
    print("\n ~ conexión establecida ~ \n")

    print("\n----------------------------------------- MENSAJES -----------------------------------------\n")
    mensaje = input("Escriba el mensaje que desea enviar: ")
    em = Emisor(mensaje)

    d = {mensaje}
    
    msg = em.enviar_objeto()


    # fixed lenght header
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    c_socket.send(msg)

   



