from random import  randint
from functools import reduce

numeros_gerados = [randint(1, 100) for _ in range(1, 100)]

maior_entre = lambda n1, n2: n1 if n1 > n2 else n2
resultado = reduce(maior_entre, numeros_gerados)
print(resultado)