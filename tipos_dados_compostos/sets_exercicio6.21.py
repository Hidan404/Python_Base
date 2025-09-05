n1 = [1,5,8,9,12,47]
n2 = [1,5,123,98,56]

intersecao = set(n1) & set(n2)
print(intersecao)

diferenca = set(n1) - set(n2)
print(diferenca)

diferenca2 = set(n2) - set(n1)
print(diferenca2 )