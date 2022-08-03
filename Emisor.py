from copyreg import pickle
from bitarray import bitarray
import numpy as np
from random import randint
import pickle

class Emisor:

    def __init__(self, cadena):
        self.cadena = cadena
        self.cadena_codificada = ''

    # capa de aplicacion
    def enviar_cadena(self):
        self.cadena

    # capa de verificacion
    def enviar_cadena_segura(self):
        cadena = self.cadena

        # codigo extraido de: https://www.geeksforgeeks.org/python-convert-string-to-binary/
        cadena_bin = ''.join(format(i, '08b') for i in bytearray(cadena, encoding ='utf-8'))

        cadena_bitarr = bitarray(cadena_bin)
        
        return cadena_bin, cadena_bitarr

    # capa de ruido
    def agregar_ruido(self):
        cadena_bin, cadena_bitarr = self.enviar_cadena_segura()
        
        for i in cadena_bin:
            posicion = randint(0, len(cadena_bin)-1)
            cadena_bin = cadena_bin[:posicion] + str(randint(0,1)) + cadena_bin[posicion+1:]
            
        print(cadena_bin)
        
        

    # capa de transmision
    def enviar_objeto(self):
        cadena_bin, cadena_bitarr = self.enviar_cadena_segura()
        # pickle.dumps(obj, protocol = None, *, fix_imports = True) 
        data_cadena =  pickle.dumps(cadena_bitarr)
        return data_cadena



