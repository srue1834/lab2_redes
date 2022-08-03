import pickle
HEADERSIZE = 10

class Receptor:
    
    def __init__(self, cadena, full_cadena, d):
        self.cadena = cadena
        self.full_cadena = full_cadena
        self.d = d
        
    # capa de transmision
    def recibir_objeto(self):
        cadena = self.cadena 
        return cadena 

    # capa de codificacion
    def codificacion(self, full_cadena):
        full_cadena = self.full_cadena

        # data_cadena =  pickle.loads(full_cadena)
        d = pickle.loads(full_cadena)
        return d

    # capa de verificacion
    def recibir_cadena_segura(self):
        self.cadena


    # capa de aplicacion
    def recibir_cadena(self):
        self.cadena

    # codigo extraido de: https://github.com/danielmuthama/Hamming-Code/blob/master/hammingcode.py
    def hamming_error_detection(self, d):
        d = self.d
        data = list(d)
        data.reverse()
        c, ch, j, r, h= 0, 0, 0, 0, []
        
        while ((len(d) + r +1) > (pow(2, r))):
            r += 1

        for i in range(0,(r + len(data))):
            p = (2**c)

            if(p == (i + 1)):
                h.append(0)
                c += 1

            else:
                h.append(int(data[j]))
                j += 1

        for parity in range(0, (len(h))):
            ph = (2**ch)
            if(ph == (parity + 1)):
                startIndex = ph-1
                i = startIndex
                toXor = []

                while(i<len(h)):
                    block = h[i:i + ph]
                    toXor.extend(block)
                    i += 2*ph

                for z in range(1,len(toXor)):
                    h[startIndex]=h[startIndex]^toXor[z]
                ch += 1

        h.reverse()
        print('\nCodigo de hamming generado:- ', end = "")
        print(int(''.join(map(str, h))))

        d = ''.join(map(str, h))
        data = list(d)
        data.reverse()
        c, ch, j, r, error, h, parity_list, h_copy = 0, 0, 0, 0, 0, [], [], []

        for k in range(0, len(data)):
            p = (2**c)
            h.append(int(data[k]))
            h_copy.append(data[k])
            if(p == (k + 1)):
                c += 1
                
        for parity in range(0, (len(h))):
            ph=(2**ch)
            if(ph==(parity+1)):

                startIndex = ph-1
                i = startIndex
                toXor = []

                while(i < len(h)):
                    block = h[i: i + ph]
                    toXor.extend(block)
                    i += 2*ph

                for z in range(1, len(toXor)):
                    h[startIndex] = h[startIndex]^toXor[z]
                parity_list.append(h[parity])
                ch += 1

        parity_list.reverse()
        error = sum(int(parity_list) * (2**i) for i, parity_list in enumerate(parity_list[::-1]))

        if((error) == 0):
            print('\nEl codigo de hamming no tiene ningun error!\n')

        elif((error) >= len(h_copy)):
            print('\nNo se pudo detectar un error :( \n')

        else:
            print('\nEl error fue ubicado en el', error,'bit\n')


           