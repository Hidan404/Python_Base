import sys


frase = "O rato roeu a roupa do rei de Roma"
c = 0
letra_pésquisar = input("Digite a letra que deseja pesquisar: ").strip().lower()
if len(letra_pésquisar) != 1:
    print("Por favor, digite apenas uma letra.")
    sys.exit()
for letra in frase.lower():
    c = frase.find("r", c)
    if c != -1:
        print(f"Letra 'r' encontrada na posição: {c}")
        c += 1
      