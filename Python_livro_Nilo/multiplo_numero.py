def numero_multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

print(numero_multiplo(8, 4))    
print(numero_multiplo(7, 3))   


import math
def quadrado(n):
    return math.pow(n, 2)

print(quadrado(5))    