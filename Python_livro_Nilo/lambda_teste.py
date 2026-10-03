lista_de_dicionarios = [
    {"nome": "Alice", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"},
    {"nome": "Breno", "idade": 28, "cidade": "Curitiba"},
]

print(lista_de_dicionarios)

lista_de_dicionarios.sort(key= lambda l: l["nome"])

list_nova = sorted(lista_de_dicionarios, key=lambda l: l["nome"])
for l in list_nova:
    print(l["nome"])


def executa(funcao, *args):
    return funcao(*args)

soma = lambda x, y: x + y

print(executa(soma, 5, 15))


print(soma(78, 25))


pessoa ={
    "Nome": "Hidan",
    "idade": 21
}

nome, idade = pessoa.values()
print(f"Nome: {nome} | idade: {idade}")


lista_multiplicados = [n * 2 for n in range(1,11)]
print(lista_multiplicados)