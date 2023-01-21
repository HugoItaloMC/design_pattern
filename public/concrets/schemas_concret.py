from abs.meta_factory import ProdutoFactory
from concrets.models_concret import Camisa, Tenis


class EstoqueCalcados(ProdutoFactory):

    def cadastrar_produto(self):
        return Tenis()

    def escolher_produto(self):
        return (...)


class EstoqueVestuario(ProdutoFactory):

    def cadastrar_produto(self):
        return Camisa()

    def escolher_produto(self):
        return (...)