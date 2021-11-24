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

print(encripta_cesar("""
Desencryptar ficheros encriptados con algoritmo de cesar
Encriptar usando mensaje secreta escondida en los ficheros (algoritmo mejorado con linear congruencia y reverso para  desencriptación.
Investigar sobre la leí de protección de datos, especialmente en lo que se refiere a necesidad de encryptacion de datos sensibles.
Hacer una presentación en grupo de 10 minutos (1) enseñando como habeis desencriptado y (2) vuelto a encriptar usando la encriptación mejorada, (3) finalmente, comentar sobre la leí de protección de datos y encryptación de datos sensibles (que datos son los sensibles y que tipo de encryptación se recomiendan). """,16))

# referencias: https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/    
# https://stackoverflow.com/questions/2911432/reversible-pseudo-random-sequence-generator

# print(help(letra_rota))
# print("A",letra_rota("A"))
# print("B",letra_rota("B"))
# print("Y",letra_rota("Y",4))
# print("Z",letra_rota("Z",5))
# print("a",letra_rota("a",6))
# print("b",letra_rota("b",semilla=7))
# print("z",letra_rota("z",semilla=8))

# Ejercicio - una función para desencriptar:
# def desencripta_cesar():
#     pass

# desencripta_cesar("Pdvwhu#gh#Uhjxodflrq#B#Edqfd#0#XQDY",3)


def random_number_and_choice(xi):
    """ Function to calculate a random number and a random choice 
        using the linear congruences method 
            input: seed as integer
            output: 
                xi_plus: integer with the random number (next seed) 
                comp_move: 0 or 1 with the computer move
    """
    a, b, m = 2491, 1, 58
    xi_plus_1 = (a * xi + b) % m
    if xi_plus_1 <= 2**31 :
        comp_move = 0
    else :
        comp_move = 1
    return comp_move, xi_plus_1


