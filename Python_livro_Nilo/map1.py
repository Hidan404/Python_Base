numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
def pares(n):
    if n % 2 == 0:
        return n
    return None


lista_pares = map(pares, numeros)
for l in lista_pares:
    if l is not None:
        print(l)