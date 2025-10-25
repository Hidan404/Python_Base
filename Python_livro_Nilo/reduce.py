from functools import reduce

lista = [10,15,2,3,4,5]

def minimo(n, m):
    if n < m:
       return n
    else:
        return m

    

print(reduce(minimo, lista))


menor = any(l == 1 for l in lista )
print(menor)