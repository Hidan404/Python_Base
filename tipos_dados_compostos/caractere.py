frase = "Eu sou poderoso e magnanimo"
dicionario = {}

for f in frase:
    dicionario[f] = dicionario.get(f,0) + 1

print(dicionario)    