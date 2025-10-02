numeros = [1,2,3,4,5,6,7,8,910,11,12,13,14,15]

def pares(a: int) -> bool:
    return a % 2 == 0

numeros_pares = filter(pares,numeros)
   
for n in numeros_pares:
    print(n)

