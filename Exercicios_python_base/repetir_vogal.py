import unidecode

def palavra_usuario():
    lista_palvras = []
    try:
        while True:
            palavra = input("Digite uma palavra: ")
            palavra_acento = unidecode.unidecode(palavra, 'utf-8')
            lista_palvras.append(repetir_vogal_(palavra_acento))

            escolha = input("Deseja continuar? (s/n): ").strip().lower()
            if escolha == "n":
                return lista_palvras
                break
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        exit()       
    


def repetir_vogal_(palavra):
    vogais = "aeiou"
    for letra in palavra:
        if letra in vogais:
            palavra = palavra.replace(letra, letra * 2)
    return palavra


palavra_vogais_repetidas = palavra_usuario()

for palavra in palavra_vogais_repetidas:
    print(palavra)