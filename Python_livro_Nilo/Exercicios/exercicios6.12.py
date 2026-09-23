lista = [1,-30,2,3,7,8,85,19,189,-87]

def menor_numero(lista: list):
    menor = 0
    maior = 0
    media = lambda lista: sum(lista) / len(lista) if lista else 0
    for i in lista:

        if menor > i:
            menor = i
        if maior < i:
            maior = i    
    print(f"Menor: {menor} | Maior: {maior}")
    print(f"Media: {media(lista)}")

menor_numero(lista)