# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import Pyro4

@Pyro4.expose
class Calculator:
    def add(self, a, b):
        return a + b

daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)

print("URI do objeto:", uri)

daemon.requestLoop()
