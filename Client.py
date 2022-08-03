'''
referencias:
    https://www.youtube.com/watch?v=Lbfe3-v7yE0
    https://youtu.be/WM1z8soch0Q

'''

import socket
import pickle
from Receptor import *

HEADERSIZE = 10

# se define el objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# en este caso el socket quiere conectar
s.connect((socket.gethostname(), 1234))

while True:

    
    full_msg = b''
    new_msg = True
    # acepta el mensaje
    while True:
        msg = s.recv(16)

        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
            
    
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            # print(full_msg[HEADERSIZE:])

            
            d = pickle.loads(full_msg[HEADERSIZE:])
            re = Receptor(msg, full_msg, d)
            print(d)

            re.hamming_error_detection(d)
            
            new_msg = True
            full_msg = b''


