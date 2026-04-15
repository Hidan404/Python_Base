#ENTRADA
#PROCESSAMENTO
#SAIDA

class PalavraContar():
    
    def __init__(self, palavra):
        self.palavra = palavra

        if not isinstance(self.palavra, str):
            raise ValueError("Palavra tem que ser string")

       

    def contar_letras(self):
        cont = 0
        for i in self.palavra:
            cont+= 1

        return f"Palavra tem {cont} letras"
    
if __name__ == "__main__":
    while True:
        palavra_usuario = input("Digite uma palavra: ").strip()
        palavra = PalavraContar(palavra_usuario)

        print(palavra.contar_letras())
        continuar = input("Digite Sim/Nao para sair: ").strip().capitalize()

        if continuar == "Sim":
            continue
        else:
            break
            