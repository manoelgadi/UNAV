# -*- coding: utf-8 -*-
"""
Spyder Editor

ALGORITMO DE CESAR
"""

def letra_rota(letra):
    """ Devuelve la letra mas uno. Input: una letra """
    num = ord(letra) - 65
    num = (num + 1) % 26 # Este el algoritimo de cesar
    num = num + 65
    return(chr(num))


msg_original = "Master de Regulacion y Banca - UNAV 2021"

msg_encriptado = "Nbtuf" # la semilla es 1

print(help(letra_rota))
print("A",letra_rota("A"))
print("B",letra_rota("B"))
print("Y",letra_rota("Y"))
print("Z",letra_rota("Z"))
print("a",letra_rota("a"))
print("b",letra_rota("b"))




