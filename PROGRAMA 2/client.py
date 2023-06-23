# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import Pyro4

uri = input("Insira aqui a URI do objeto Calculator: ")

calculator = Pyro4.Proxy(uri)

num1 = int(input("Insira aqui o primeiro número: "))
num2 = int(input("Insira aqui o segundo número: "))

resultado = calculator.add(num1, num2)

print("Resultado:", resultado)
