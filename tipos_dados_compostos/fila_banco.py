import sys

ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))

try:
    while True:
        print(f'Pessoas na fila: {len(fila1)}')
        print(f'Pessoas na fila 2: {len(fila2)}')
        print(f'Fila atual: {fila1}')
        print(f"Fila 2 atual: {fila2}")
        print("Dgite F para adicionar um cliente ao fim da fila 1")
        print("Dgite G para adicionar um cliente ao fim da fila 2")
        print("Dgite A para atender um cliente da fila 1 ou S para sair")
        print("Digite B para atender um cliente da fila 2")

        operacao = input("Operação (F,G,A,B ou S): ").strip().upper()
        print(operacao)
        for oper in operacao:
            if oper == "A":
                if len(fila1) > 0:
                    atendido = fila1.pop(0)
                    print(f'Cliente {atendido} foi atendido.')
                else:
                    print("Fila vazia! Ninguém para atender.")
            elif oper == "B":
                if len(fila2) > 0:
                    atendido = fila2.pop(0)
                    print(f'Cliente {atendido} foi atendido.')
                else:
                    print("Fila vazia! Ninguém para atender.")
            elif oper == "G":
                ultimo += 1
                fila2.append(ultimo)
                print(f'Cliente {ultimo} entrou na fila.')        
            elif oper == "F":
                ultimo += 1
                fila1.append(ultimo)
                print(f'Cliente {ultimo} entrou na fila.')
            elif oper == "S":
                print("Encerrando o programa.")
                sys.exit()
            else:
                print("Operação inválida! Tente novamente.")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")                