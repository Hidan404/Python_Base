def faixa(inicio = 0, fim = 10, passo = 1):
    """Gera uma sequência de números inteiros"""
    numero = inicio
    while numero < fim:
        yield numero
        numero += passo

print(list(faixa(1)))       


def fatorial(n):
    """Calcula o fatorial de n"""
    fat = 1
    for i in faixa(1, n + 1):
        fat *= i
        yield fat


for numero, valor in enumerate(fatorial(10)):
    print(f'{numero + 1}! = {valor}')        
    