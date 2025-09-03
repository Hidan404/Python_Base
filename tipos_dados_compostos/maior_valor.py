lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maior = lista[0]
menor = lista[0]
contador = 0
total = 0

for valor in lista:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    total += valor
    contador += 1     



print(f'O maior valor da lista é {maior}')
print(f'O menor valor da lista é {menor}')
print(f'A média dos valores da lista é {total / contador}')