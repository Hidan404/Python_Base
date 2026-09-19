ultimoA = 10
ultimoB = 10
fila = list(range(1, ultimoA + 1))
fila2 = list(range(1, ultimoB + 1))
# print(fila)

while True:
    print(f"Clientes na fila {len(fila)}")
    print(f"Fila atual {fila}")

    print(f"Clientes na fila 2 {len(fila2)}")
    print(f"Fila atual {fila2}")

    print("Digite F para adicionar na fila")
    print("Digite R para remover e S para sair")

    print("Digite G para adicionar na fila 2")
    print("Digite Q para remover e S para sair")

    opcao = input("Opçao: ").upper().strip()

    if opcao in ("F", "G"):
        if opcao == "F":
            ultimoA+= 1
            fila.append(ultimoA)
        else:
            ultimoB+= 1
            fila2.append(ultimoB)
    elif opcao in ("R", "Q"):
        fila_selecionada = fila if opcao == "R" else fila2
        if not fila_selecionada:
            print(f"Fila nao tem mais ninguem {len(fila_selecionada)}")
        else:
            fila_selecionada.pop()
    elif opcao.startswith("S"):
        print("Saindo...")
        break

print(f"Clientes restantes {len(fila)}")
