from json_pessoa import ArquivoJsonPessoa


class Main():
    def __init__(self):
        arquivo_json_pessoa = ArquivoJsonPessoa()
        arquivo_json_pessoa.salvar_arquivo()

if __name__ == "__main__":
    Main()        