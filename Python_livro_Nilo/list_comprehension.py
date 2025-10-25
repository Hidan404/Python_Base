numeros = [1,2,3,4,5,6]

dobro = [d * 2 for d in numeros]
print(dobro)

lista_tuplas = [(x, x * 2) for x in numeros]
print(lista_tuplas)

desempacotar = [y for x in lista_tuplas for y in x]
print(desempacotar)


import math

raiz_perfeita = [x for x in numeros if math.sqrt(x) % 1 == 0]
print(raiz_perfeita)