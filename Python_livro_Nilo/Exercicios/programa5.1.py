


def cedulas_valor():
    valor = round(float(input("Digite o valor: ")) * 100)
    denominacoes = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 2, 1]
    atual = denominacoes[0]
    cedulas = 0
    apagar = valor


    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            print(f"Cédulas/moedas: {cedulas} | Atual: R$ {atual / 100:.2f}")

            if apagar == 0:
                opcao = input("Deseja continuar S/N: ").upper().strip()
                if opcao == "S":
                    cedulas_valor()
                    continue
                break

            if atual == denominacoes[-1]:
                break

            atual = denominacoes[denominacoes.index(atual) + 1]
            cedulas = 0


cedulas_valor()

                    