from abs.models_abs import Calcados, Vestuario


class Tenis(Calcados):

    @classmethod
    def label(cls, Tenis):
        cls.nome = Tenis.nome
        cls.preco = Tenis.preco
        cls.size = Tenis.tamanho


    def __init__(self, nome: str, preco: float, size):
        self.nome = nome
        self.preco = preco
        self.size = size



class Camisa(Vestuario):

    @classmethod
    def label(cls, Camisa):
        cls.nome = Camisa.nome
        cls.preco = Camisa.preco
        cls.size = Camisa.size

    def __init__(self, nome: str, preco: float, size: str):
        self.nome = nome
        self.preco = preco
        self.size = size

