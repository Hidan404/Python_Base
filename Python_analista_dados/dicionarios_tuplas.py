bandas_musicas = [
    {"banda": "the gazette", "musica": ("filth in the beauty", "description"), "duracao": "4:00"},
    {"banda": "the gazette", "musica": ("cassis", "description"), "duracao": "4:30"},
    {"banda": "the gazette", "musica": ("leech", "description"), "duracao": "3:45"},
    {"banda": "the gazette", "musica": ("vortex", "description"), "duracao": "5:15"},
]

for banda in bandas_musicas:
    print(f"A banda {banda['banda']} tem a música {banda['musica']} com duração de {banda.get('duracao', 'desconhecida')}")

for banda in bandas_musicas:
    for chave, valor in banda.items():
        print(f"{chave}: {valor[0] if isinstance(valor, tuple) else valor}")
        duracao = int(banda.get('duracao', '0:00').split(':')[0]) * 60 + int(banda.get('duracao', '0:00').split(':')[1])
        maior_duracao = 0
        if duracao > maior_duracao:
            maior_duracao = duracao
            musica_mais_longa = banda['musica'][0]

print(f"A música mais longa é {musica_mais_longa} com duração de {maior_duracao // 60}:{maior_duracao % 60:02d}")            




akatsuki = ("konan", "pain","hidan","kakuzu")
akatsuki_nova = []
for i in akatsuki:
    if i == "konan":
        akatsuki_nova = ["sasori" if i == "konan" else "konan"]
        continue
    akatsuki_nova.append(i)    

print(akatsuki_nova)     


lista = [120, "python", 120.01, "asw", False, [10, 20]]

def trabalhar_na_lista():
    retorno = []
    if lista:
        retorno.append(lista[-1])
    if lista:
        retorno.append(lista[0])
    if lista:
        retorno.append(lista[-1][1])      

    return retorno
print(trabalhar_na_lista())              
        

produtos = {}

def adicoanr_no_objeto():
    while True:
        nome  = input("Digite nome:")
        preco = float(input("Digite o preco: "))
        novo_produto = {"nome": nome, "preco": preco}
        produtos.update(novo_produto)
        opcao = input("Digite [S] para sair: ").upper().strip()
        if opcao == "S":
            break

    return produtos    

#print(adicoanr_no_objeto())    


frase = {}

def contar_frases():
    while True:
        texto = input("Digite: ")
        if texto == "":
            break

        if texto not in frase:
            frase[texto] = 1
        else:
            frase[texto]+= 1

        
    for i in frase:
        print(f"{i} > {frase[i]}")        

contar_frases()