def lista_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Digite um número (ou -1 para sair): "))
            if num == -1:
                break
            numeros.append(num)
        except ValueError:
            print("Por favor, digite um número válido.")
    return numeros


def maior_numero(numeros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

if __name__ == "__main__":
    numeros = lista_numeros()

    if numeros:
        maior = maior_numero(numeros)
        print(f"O maior número digitado foi: {maior}")    