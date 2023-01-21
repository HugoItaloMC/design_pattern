from abc import ABCMeta, abstractmethod

class ProdutoFactory(metaclass=ABCMeta):
    # Factory
    @abstractmethod
    def cadastrar_produto(self):
        (...)

    @abstractmethod
    def escolher_produto(self):
        (...)
