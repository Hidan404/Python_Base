def soma(a, b):
    return lambda c: c + a + b

somar = soma(10, 15)

resultado = somar(30)
print(resultado)

