import sys

print(sys.argv)
print(sys.platform)

lista_palavras = ["Naruto", "Sasuke", "Kakashi", "Itachi", "Jiraiya", "Tsunade", "Gaara", "Rock Lee"]

for item in lista_palavras:
    with open("i/o.py/dados.txt", "a") as f:
        f.write(f"{item}\n")
  