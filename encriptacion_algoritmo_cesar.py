# -*- coding: utf-8 -*-
"""
Spyder Editor

ALGORITMO DE CESAR
"""

def letra_rota(letra,semilla=1):
    """ Devuelve la letra mas uno. Input: una letra """
    num = ord(letra) + semilla
    if(num >122):
        num = num - 58 # Este el algoritimo de cesar
    return(chr(num))

def encripta_cesar(msg_original,semilla=1):
    """ Encripta un texto usando algoritmo de cesar. """
    msg_encriptado = "" # la semilla es 1
    
    for caracter in msg_original:
    #    print(caracter,letra_rota(caracter,2))
        msg_encriptado = msg_encriptado + letra_rota(caracter,semilla)
    return(msg_encriptado)
    



print("Master de Regulacion y Banca - UNAV")

print(encripta_cesar("Master de Regulacion y Banca - UNAV",3))

    
# print(help(letra_rota))
# print("A",letra_rota("A"))
# print("B",letra_rota("B"))
# print("Y",letra_rota("Y",4))
# print("Z",letra_rota("Z",5))
# print("a",letra_rota("a",6))
# print("b",letra_rota("b",semilla=7))
# print("z",letra_rota("z",semilla=8))

# Ejercicio - una función para desencriptar:
#def desencripta_cesar():
#    pass

#desencripta_cesar("Pdvwhu#gh#Uhjxodflrq#B#Edqfd#0#XQDY",3)

lo_que_hay_que_hacer = """TuIuDsHOFJqH0vysxuHEI0uDsHyFJqtEI0sED0qBwEHyJCE0tu0suIqHUDsHyFJqH0KIqDtE0CuDIqzu0IusHuJq0uIsEDtytq0uD0BEI0vysxuHEI08qBwEHyJCE0CuzEHqtE0sED0ByDuqH0sEDwHKuDsyq0O0HuLuHIE0FqHq00tuIuDsHyFJqsyÉD>YDLuIJywqH0IErHu0Bq0BuÃ0tu0FHEJussyÉD0tu0tqJEI<0uIFusyqBCuDJu0uD0BE0GKu0Iu0HuvyuHu0q0DusuIytqt0tu0uDsHOFJqsyED0tu0tqJEI0IuDIyrBuI>XqsuH0KDq0FHuIuDJqsyÉD0uD0wHKFE0tu0A@0CyDKJEI08A90uDIuÇqDtE0sECE0xqruyI0tuIuDsHyFJqtE0O08B90LKuBJE0q0uDsHyFJqH0KIqDtE0Bq0uDsHyFJqsyÉD0CuzEHqtq<08C90vyDqBCuDJu<0sECuDJqH0IErHu0Bq0BuÃ0tu0FHEJussyÉD0tu0tqJEI0O0uDsHOFJqsyÉD0tu0tqJEI0IuDIyrBuI08GKu0tqJEI0IED0BEI0IuDIyrBuI0O0GKu0JyFE0tu0uDsHOFJqsyÉD0Iu0HusECyuDtqD9>0"""
# referencias: https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/    
# https://stackoverflow.com/questions/2911432/reversible-pseudo-random-sequence-generator

"""
Method of linear congruences
Given an initial number , known as seed, the number of the sequence x1 is given by
x1=(ax0+b) mod (m). In general form, the xi+1 number is obtaining from the previous number xiusing
the formula xi+1=(axi+b) mod (m). mod is the modulo operator1
For example, for a = 7, b = 1, m = 13 and x0=3, the sequence of numbers generated is: 9, 12, 7,
11, 0, 1, 8, 5, 10, 6, 4, 3, 9, ...
In this IPE, you must use as parameters the values a=231, b=1 e m=50, which are used
by known systems
"""


