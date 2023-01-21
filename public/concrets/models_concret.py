from abs.models_abs import Calcados, Vestuario


class Tenis(Calcados):

    def __init__(self, nome: str, preco: float, size):
        self.nome = nome
        self.preco = preco
        self.size = size

    def label(self, Tenis):
        self.nome = Tenis.nome
        self.preco = Tenis.preco
        self.size = Tenis.tamanho


class Camisa(Vestuario):

    def __init__(self, nome: str, preco: float, size: str):
        self.nome = nome
        self.preco = preco
        self.size = size

    def label(self, Camisa):
        self.nome = Camisa.nome
        self.preco = Camisa.preco
        self.size = Camisa.size

