import operator
from functools import partial, reduce


def executa(operacao,simbolo,*Operandos):
    resultado = reduce(operacao, Operandos)
    print(f"{Operandos} {simbolo} = {resultado}")


def operacoes():
    operacoes_ = {
        "+": partial(executa,operator.add, "+")
    } 

    return operacoes_   

def main():
    operacoes_fincao = operacoes()
    while True:
        operandos_usuario = input("Digite numeros seprados por virgula: ").split(",")
        operandos_usuario = [float(numeros) for numeros in operandos_usuario]
        operation = input("Digite uma operação: ").strip()

        if operation in operacoes_fincao:
            operacoes_fincao[operation](*operandos_usuario)
        else: 
            print("Não tem numeros validos")    


if __name__ == "__main__":
    main()