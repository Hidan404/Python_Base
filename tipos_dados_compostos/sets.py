numeros1 = set([1,8,9,10])
numeros2 = set([1,5,12,10])

uniao = numeros1 | numeros2
print(uniao)

intersecao = numeros1 & numeros2
print(intersecao)

diferenca = numeros1 - numeros2
print(diferenca)
diferenca2 = numeros2 - numeros1
print(diferenca2)