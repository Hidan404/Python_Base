import string

frase = """Esta é uma frase
quebrada em várias linhas."""

def contar_letras_qtd():
    contador = {}
    try:
        escolha_usuario = input("Digite uma letra: ").lower()
        
        if escolha_usuario in string.ascii_lowercase and len(escolha_usuario) == 1:
            for i in frase.lower():
                if i != " " and i != "." and i != " \n":
                    if i == escolha_usuario:
                        contador[i] = contador.get(i, 0) + 1
        else:
            print("digite letras")            
        
        print(contador)    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")
        

contar_letras_qtd()    