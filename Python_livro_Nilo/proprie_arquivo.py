import os
import os.path
import time
import sys

nome = sys.argv[1]
agora = time.localtime()
def propriedades(arg):
    print(f"Nome: {arg}")
    print(f"Tamanho {os.path.getsize(arg)}")
    print(f"Criado {time.ctime(os.path.getctime(arg))}")
    print(f"Modificado {time.ctime(os.path.getmtime(arg))}")
    print(f"Acessado {time.ctime(os.path.getatime(arg))}")


if __name__ == "__main__":
    propriedades(nome)    