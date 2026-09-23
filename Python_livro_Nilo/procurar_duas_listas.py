lista2 = [3, 5, 8, 10, 2, 4, 8, 9]

achar1 = int(input("Digite um numero: "))
achar2 = int(input("Digite um numero: "))
contador = 0

for i in lista2:
    contador+= 1
    if achar1 == i:
        print(f"Contador {contador} {achar1} |")
    if achar2 == i:
        print(f"Contador {contador} {achar2} |")

for i, v in enumerate(lista2):
    print(f"Indice: {i} | Valor: {v}")