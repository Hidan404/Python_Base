numeros = [4,5,8,79,46,12,18,32]
pares = []
impares = []

for i, n in enumerate(numeros):
    if n % 2 == 0:
        pares.append(f"{i} = {n}")
    else:    
        impares.append(f"{i} = {n}")


print(f"Pares {pares}")
print(f"Impares: {impares}")