# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import Pyro4

uri = "PYRONAME:string_inverter"
string_inverter = Pyro4.Proxy(uri)

string = input("Digite aqui a string a ser invertida: ")

inverted_string = string_inverter.invert_string(string)

print("String invertida:", inverted_string)
