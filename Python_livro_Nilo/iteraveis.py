lista = ["hidan", "konan", "kakashi", "naruto", "sasuke"]

iterar = lista.__iter__()

for i in range(len(lista)):
    try:
        print(next(iterar))
    except StopIteration:
        print("Fim da iteração")   


def generator():
    for i in range(10):
        yield i
                   

print(list(generator()))        


from pathlib import Path

caminho = Path(__file__).parent / "entrada.txt"
def abrir_arquivo() -> str:
    with open(caminho, "r") as arquivo:
        for linha in arquivo:
            yield linha.strip()

print(list(abrir_arquivo()))            

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5    

for i in gen2():
    print(i)    