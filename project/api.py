from typing import Any

from tornado import httputil

from model import Calcados
from interfaces.pagine import APIMeta, Page


class Index(Page, Calcados):

    def __init__(self, application: (Calcados, Page), request: httputil.HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)

    def home_2handler(self):
        self.manager(opp='GETS')
        self.render('index.html', produto=self.produto)

    def new_2handler(self):
        self.render('new.html')

    def update_2handler(self):
        self.render('update.html')

    def service(self, opp: int):
        while (op := opp != None):
            if op == 1:
                return self.home_2handler()
            elif op == 2:
                return self.new_2handler()
            elif op == 3:
                return self.update_2handler()
            else:
                ...



class API(APIMeta, Index):

    def _post(self):

        produto: object = Calcados

        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        produto.first_name = nome
        produto.mind_name = marca
        produto.last_name = modelo
        produto.price = preco
        produto.size = tamanho
        produto.manager(opp='POST')
        self.redirect('index.html')

    def _put(self, id):

        produto: Calcados = Calcados
        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        produto.first_name = nome
        produto.mind_name = marca
        produto.last_name = modelo
        produto.price = preco
        produto.size = tamanho

        produto.manager('PUT')
        self.redirect('index.html')

    def _remove(self, id):
        produto: Calcados = Calcados()
        produto.get_an(id)
        produto.manager('DELETE')
        self.redirect('index.html')
