def multi_soma():
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um numero: "))

    soma = 0

    for i in range(1, int(numero1 + 1)):
        soma+= numero2

    return soma

#print(multi_soma())


def div_subtrair():
    numero1 = float(input("Digite um numero: "))
    while numero1 <= 0:
        numero1 = float(input("Digite um numero maior que zero: "))

    numero2 = float(input("Digite um numero: "))
    while numero2 <= 0:
        numero2 = float(input("Digite um numero maior que zero: "))

    subtrair = numero2
    contador = 0
    resto = numero1

    while resto >= subtrair:
        resto -= subtrair
        contador += 1

    print(f"quociente: {contador}")
    print(f"resto: {resto}")

    return contador, resto

print(div_subtrair())    