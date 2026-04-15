from banco import Banco
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


def menu():
    print("\n=== BANCO ===")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Adicionar conta")
    print("5 - Listar contas")
    print("0 - Sair")


def main():
    banco = Banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                cliente = Cliente(idade, nome)
                banco.adicionar_cliente(cliente)
                print("Cliente adicionado com sucesso!")

            elif opcao == "2":
                banco.listar_clientes()

            elif opcao == "3":
                nome = input("Nome do cliente: ")
                cliente = banco.buscar_cliente(nome)

                if cliente:
                    print(f"Nome: {cliente.nome}, Idade: {cliente.idade}")
                else:
                    print("Cliente não encontrado.")

            elif opcao == "4":
                nome = input("Nome do cliente: ")
                tipo = input("Tipo de conta (corrente/poupanca): ")

                if tipo == "corrente":
                    conta = ContaCorrente()
                elif tipo == "poupanca":
                    conta = ContaPoupanca()
                else:
                    print("Tipo inválido.")
                    continue

                banco.adicionar_conta_cliente(nome, conta)
                print("Conta adicionada com sucesso!")

            elif opcao == "5":
                nome = input("Nome do cliente: ")
                banco.listar_contas(nome)

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()

