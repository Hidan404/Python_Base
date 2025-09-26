def gerador_pares():
    numeros = 0
    while True:
        if numeros % 2 == 0:
            yield numeros
        numeros+= 1 


numeros_pares = gerador_pares()


for i in range(1, 20):
    print(next(numeros_pares))



