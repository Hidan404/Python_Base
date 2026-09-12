def tabela_precos():
    tabela = {
        1: 0.50,
        2: 1.00,
        3: 4.00,
        5: 7.00,
        9: 8.00
    }

    calculo = 0

    while True:
        codigo = int(input("Digite o codigo: "))

        qtd = int(input("Digite de qtd: "))

        if codigo not in tabela.keys():
            print("vai")
            break
        calculo+= tabela[codigo] * qtd
        continuar = input("Deseja sair S/N: ").upper().strip()
        if continuar.startswith("S"):
            print("Saindo...")
            break

    return calculo
        
        


print(tabela_precos())