def soma(a, b):
    return lambda c: c + a + b

somar = soma(10, 15)


valores = [10, 15, 20, 25, 30]
resultados = list(map(somar, valores))
resultados_filtrados = list(filter(lambda x: x > 40, resultados))
print(resultados_filtrados)

