frase = "Hidan".center(11,".")
print(frase)

rato = "O Rato roeu a roupa do rei de Roma"
rato = rato.split()
for palavra in rato:
    print(palavra.center(20,"-"))
    print(palavra.replace("a","@").center(20,"-"))


texto = " ".isspace()
print(frase.isprintable())
print(texto)    