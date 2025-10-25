import operator, math
from functools import partial, reduce


def executa(operacao,simbolo,*Operandos):
    try:
        if operacao == math.sqrt and len(Operandos) == 1:
            resultado = operacao(Operandos[0])    
        else:    
            resultado = reduce(operacao, Operandos)

        print(f"{Operandos} {simbolo} = {resultado}")
    except Exception as e:
        print(f"Erro: {e}") 



def operacoes():
    operacoes_ = {
        "+": partial(executa,operator.add, "+"),
        "-": partial(executa, operator.sub, "-"),
        "*": partial(executa, operator.mul, "*"),
        "/": partial(executa, operator.truediv, "/"),
        "sqrt": partial(executa,math.sqrt, "sqrt")
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