def media_qtd_soma():
    
    contador = 0
    soma = 0

    while True:
        numero = int(input("Digite qual quer numero e 0 para sair: "))
        if numero == 0:
            break
        contador+= 1
        soma+= numero


    return soma, contador    

print(media_qtd_soma())