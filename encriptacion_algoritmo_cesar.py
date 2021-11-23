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

lo_que_hay_que_hacer = """YDLuIJywqH0IErHu0Bq0BuO0tu0FHEJussyED0tu0tqJE0O0WT`b<0zKIJyvysqH0FEHGKu0JuDuyI0GKu0CuzEHqH0uB0qBwEHyJCE0tu0suIqH>0`HuFqHqH0KDq0FHuIuDJqsyED0tu0A@0CyDKJEI0KIqDtE0`EMuH`EyDJ0O0`OJxED>0"""

