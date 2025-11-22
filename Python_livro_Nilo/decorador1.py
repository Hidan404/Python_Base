import functools

def calc(cfuncao):
    @functools.wraps(cfuncao)
    def wrapper(*args, **kwargs):
        funcao = cfuncao(*args, **kwargs)
        return funcao
    return wrapper


@calc
def executar(a, b):
    return a + b

rersultado = executar(10, 20, 23)
print(rersultado)