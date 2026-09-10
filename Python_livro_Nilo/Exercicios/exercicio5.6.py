def tabuada_mult():
    numero_entrada = int(input("digite um numero: "))
    limite = 1

    while limite <= 10:
        print(f"{numero_entrada} x {limite} = {numero_entrada * limite}")
        limite+= 1

tabuada_mult()        