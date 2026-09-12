valor = int(input("Digite o valor: "))
atual = 100
cedulas = 0
apagar = valor

while True:
    if atual <= apagar:
        apagar-= atual
        cedulas+= 1
    else:
        print(f"Cedulas: {cedulas} | Atual: {atual}")  
        if apagar == 0:
            break
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1    

        cedulas = 0

                    