f1 = "AABECTRE"
f2 = "BE"
c= 0

for letra in f1:
    c = f1.find(f2, c)
    if c != -1:
        print(f"Letra '{f2}' encontrada na posição: {c} de {f1}")
        c += 1