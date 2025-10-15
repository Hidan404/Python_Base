from arquivos import SalvarArquivos
from agenda_telefones import Agenda


class Ui(SalvarArquivos, Agenda):
    def __init__(self):
        super().__init__()
        