
'''
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resultado = n1 + n2
print(f"A soma é: {resultado}")


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
print(f"A média é: {media:.2f}")


numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é Par")
else:
    print("O número é Ímpar")


a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
c = float(input("Terceiro número: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"O maior número é: {maior}")



celsius = float(input("Temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

'''

dinheiro_usuario = int(input("Digite um valor; "))
notas50 = dinheiro_usuario // 50
resto = notas50 % 50
print(resto)

