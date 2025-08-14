import os

def path_root():
    return os.path.join(os.path.dirname(__file__))

def listar_dir_atual():
    return os.listdir(path_root())

print(listar_dir_atual())
    
    