# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import Pyro4

class StringInverter(object):
    def invert_string(self, string):
        return string[::-1]

daemon = Pyro4.Daemon()  
ns = Pyro4.locateNS()  
uri = daemon.register(StringInverter()) 

ns.register("string_inverter", uri)

print("O Servidor está pronto para receber solicitações.")

daemon.requestLoop()
