from abs.meta_factory import ProdutoFactory
from concrets.models_concret import Camisa, Tenis


class EstoqueCalcados(ProdutoFactory):

    def cadastrar_produto(self):
        nome = input(':: Nome : ')
        preco = float(input(':: Preco : '))
        tamanho = input(':: Tamanho : ')
        return Tenis(nome, preco, tamanho)

    def escolher_produto(self):
        return (...)


class EstoqueVestuario(ProdutoFactory):

    def cadastrar_produto(self):
        nome = input(':: Nome : ')
        preco = float(input(':: Preco : '))
        tamanho = input(':: Tamanho : ')
        return Camisa(nome, preco, tamanho)

    def escolher_produto(self):
        return (...)