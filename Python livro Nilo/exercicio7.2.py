f1 = "AAACTBF"
f2 = "CTB"
f3 = ""


for letra in f1:
    f2 = f2.find(f1, f3)
    if f3 != -1:
        print(f"Letra '{f2}' encontrada na posição: {f3} de {f1}")
        f1 = f1[f3 + 1]

print(f3)        