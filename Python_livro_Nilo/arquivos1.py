import os 

def root_path():
    ROOT_PATH = os.path.join(os.path.dirname(__file__), "numeros.txt")
    return ROOT_PATH

def escrever_numeros():
    caminho = root_path()

    with open(caminho, "a") as f:
        for i in range(1,11):
            f.write(f"{str(i)}\n")

def ler():
    caminho = root_path()
    with open(caminho, "r") as f:
        for l in f.readlines():
            print(l)            

def main():
    escrever_numeros()
    ler()

if __name__ == "__main__":
    main()            