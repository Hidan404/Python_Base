import math
import random

def sortear(lista: list)-> list:
    random.shuffle(lista)
    return lista

def numeros_aleatorios(lista: list) -> list:
    lista_random = sortear(lista)
    selecionados = []
    for l in lista_random:
        if len(selecionados) < 5:
            if l > 10:
                selecionados.append(math.ceil(l))
            else:
                selecionados.append(math.floor(l))    
    return selecionados   


lista_numeros = [5.55, 4.3333, 5,8, 78.87,10,124,56,89,478,1.5698]

if __name__ == "__main__":
    print(numeros_aleatorios(lista_numeros))