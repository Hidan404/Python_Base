import sys

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

def main():
    # Tentativa de pegar argumentos da linha de comando
    if len(sys.argv) >= 3:
        try:
            nome = sys.argv[1]
            # Verifica se o segundo argumento é um número
            if not sys.argv[2].isdigit():
                print("Idade deve ser um número.")
                return
            
            idade = int(sys.argv[2])
        except ValueError:
            print("Erro ao converter idade para número.")
            return
        
    elif len(sys.argv) == 2:
        nome = sys.argv[1]
        idade = input("Digite a idade: ").strip()
    else:
        # Se não tiver argumentos suficientes, pede no input
        try:
            nome = input("Digite o nome: ").strip()
            idade = int(input("Digite a idade: ").strip())
        except ValueError:
            print("Erro ao converter idade para número.")
            return

    p = Pessoa(nome, idade)
    p.mostrar()
    print(type(p.idade))

if __name__ == '__main__':
    main()

    